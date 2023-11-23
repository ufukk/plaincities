import csv
import json
from typing import List, Iterable, Dict, Any
from pathlib import Path
import pickle

def report(msg: str, end='\n'):
    print(msg, end=end)

def skip_comments(gen):
    for row in gen:
        if not row[0].startswith('#'):
            yield row

def dump(obj):
    return json.dumps(obj, ensure_ascii=False)

def parent_code(*args):
    return '.'.join([a for a in args if a is not None and len(a)])

class NameFactory:

    @classmethod
    def from_row(cls, row: List[str]) -> "NameRow":
        values = {
            'geoid': int(row[1]),
            'lang_code': row[2],
            'name': row[3],
            'is_preferred': row[4].strip() == '1'
        }
        return NameRow(**values)

class CountryFactory:

    @classmethod
    def from_row(cls, row: List[str]) -> "CountryRow":
        values = {
            'geoid': int(row[16]),
            'alpha2': row[0],
            'alpha3': row[1],
            'fips': int(row[2]),
            'name': row[4],
            'capital': row[5],
            'area_sqm2': float(row[6]),
            'population': int(row[7]),
            'continent': row[8],
            'currency': row[10],
            'languages': row[15]
        }
        return CountryRow(**values)

class CityFactory:

    @classmethod
    def from_row(cls, row: List[str]) -> "CityRow":
        values = {
            'geoid': int(row[0]),
            'name': row[1],
            'ascii_name': row[2],
            'alternate_names': row[3].split(','), 
            'latitude': float(row[4]), 
            'longitude': float(row[5]),
            'country_code': row[8],
            'population': int(row[14]),
            'altitude': row[15] or -1,
            'timezone': row[17],
            'dem': int(row[16]),
            'feature_class': row[6],
            'feature_code': row[7]
        }
        if values['altitude'] != -1:
            values['altitude'] = int(values['altitude'])
        values['parent_code'] = parent_code(values['country_code'], row[10], row[11])
        return CityRow(**values)

class AdminCodeFactory:

    @classmethod
    def from_row(cls, row: List[str]) -> "AdminCodeRow":
        values = {'geoid': int(row[3]),
                  'code': row[0],
                  'name': row[1],
                  'ascii_name': row[2]
        }
        values['country_code'] = values['code'][0:2]
        return AdminCodeRow(**values)

class NameRow:

    def __init__(self, geoid, lang_code, name, is_preferred) -> None:
        self.geoid = geoid
        self.lang_code = lang_code
        self.name = name
        self.is_preferred = is_preferred

    def __str__(self):
        return f'{self.geoid}, {self.lang_code}, {self.name}'

class CountryRow:
    
    def __init__(self, geoid, name, alpha2, alpha3, fips, capital, continent, area_sqm2, population, currency, languages) -> None:
        self.geoid = geoid
        self.name = name
        self.alpha2 = alpha2
        self.alpha3 = alpha3
        self.fips = fips
        self.capital = capital
        self.area_sqm2 = area_sqm2
        self.continent = continent
        self.population = population
        self.languages = languages
        self.currency = currency

    def update(self, names: List[NameRow]):
        if len(names):
            self.name = names[0].name

class CityRow:

    def __init__(self, geoid, name, ascii_name, alternate_names, latitude, longitude, country_code, population, dem, feature_class, feature_code, timezone, altitude, parent_code) -> None:
        self.geoid = geoid
        self.name = name
        self.ascii_name = ascii_name
        self.alternate_names = alternate_names
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = country_code
        self.population = population
        self.dem = dem
        self.timezone = timezone
        self.altitude = altitude
        self._feature_class = feature_class
        self._feature_code = feature_code
        self._parent_code = parent_code

    def __str__(self):
        return f'<{self.geoid}>: {self.name}'

    def update(self, names: List[NameRow]):
        if len(names):
            self.name = names[0].name
        if len(names) > 1:
            self.alternate_names = [n.name for n in names[1:]]
        if self.name == self.ascii_name:
            self.ascii_name = 0

class AdminCodeRow:

    def __init__(self, geoid, code, name, ascii_name, country_code) -> None:
        self.geoid = geoid
        self.code = code
        self.name = name
        self.ascii_name = ascii_name
        self.country_code = country_code
    
    def update(self, names: List[NameRow]):
        if len(names):
            self.name = names[0].name


def rowlist_to_template(names: Iterable[str], rows: Iterable[Any], **kwargs):
    tpl = []
    for key in names:
        if key.startswith('__') or key in ['update']:
            continue
        tpl.append(f'{key}_list = {dump([getattr(x, key) for x in rows])}')
    for key, val in kwargs.items():
        tpl.append(f'{key} = {dump(val)}')
    return '\n'.join(tpl)

def write_constants(output, default_lang, available_languages, timezones):
    with open(output, 'w') as fp:
        fp.write(f"""default_language = "{default_lang}"
available_languages = {dump(available_languages)}
timezone_names = {dump(timezones)}
""")

class AlternateNamesReader:

    def __init__(self, path) -> None:
        self.cache_file = path.parent / 'names.cache'
        self.fp = open(path, 'r')
        self.file_size = path.stat().st_size
        self.id_map: Dict[str, List[NameRow]] = {}

    def save_cache_file(self):
        with open(self.cache_file, 'wb') as fp:
            pickle.dump(self.id_map, fp)

    def load_cache_file(self):
        if self.cache_file.exists():
            with open(self.cache_file, 'rb') as fp:
                self.id_map = pickle.load(fp)
                return True
        else:
            return False

    def ensure_names(self):
        report('building names...')
        if len(self.id_map) > 0:
            return
        if self.load_cache_file():
            report(f'loaded from cache!')
            return
        self.fp.seek(0)
        last_pos = -1
        while True:
            line = self.fp.readline()
            if not line:
                break
            name_row = NameFactory.from_row(line.split('\t'))
            if not name_row.lang_code or name_row.lang_code == 'link':
                continue
            if name_row.geoid not in self.id_map:
                self.id_map[name_row.geoid] = []
            self.id_map[name_row.geoid].append(name_row)
            pos = round(self.fp.tell() / self.file_size, ndigits=2) * 100
            if last_pos != pos:
                last_pos = pos
                report(f'Building cache: {round(last_pos)}%', end='\r')
        self.fp.close()
        self.save_cache_file()

    def read_names_for(self, place_id, selected_lang):
        names = [n for n in self.id_map[place_id] if n.lang_code == selected_lang] if place_id in self.id_map else []
        return sorted(names, key=lambda a: (a.is_preferred, a.name), reverse=True)

class Generator:

    alternate_names_file = 'alternateNamesV2.txt'
    countries_file = 'countryInfo.txt'
    states_file = 'admin1CodesASCII.txt'
    districts_file = 'admin2Codes.txt'

    def __init__(self, input_path, output_path) -> None:
        self.input_path = self.path_for(input_path)
        self.output_path = self.path_for(output_path)
        self.name_reader = AlternateNamesReader(self.input_path / self.alternate_names_file)
        self.timezone_names = None

    @classmethod
    def path_for(cls, path):
        return Path(path) if not isinstance(path, Path) else path

    def read_admin_codes(self, input, lang) -> Dict[str, Dict[str, AdminCodeRow]]:
        countries = {}
        with open(self.input_path / input, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            for row in skip_comments(reader):
                admin_row = AdminCodeFactory.from_row(row)
                names = self.name_reader.read_names_for(admin_row.geoid, lang)
                admin_row.update(names)
                countries[admin_row.country_code] = {} if admin_row.country_code not in countries else countries[admin_row.country_code]
                countries[admin_row.country_code][admin_row.code] = admin_row
        return countries

    def read_country_codes(self, input):
        with open(self.input_path / input, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            codes = []
            for row in skip_comments(reader):
                country = CountryFactory.from_row(row)
                codes.append(country.alpha2)
            return sorted(codes) 

    def dump_admincodes(self, items: Dict[str, AdminCodeRow]):
        return {k: [v.name, v.ascii_name, v.geoid] for k, v in items.items()}

    def generate_package(self):
        with open(self.output_path / '__init__.py', 'w'):
            pass

    def generate_countries(self, lang):
        def _generate_continent_indexes(countries: List[CountryRow]):
            last_continent = None
            continent_indexes = []
            for i, country in enumerate(countries):
                if country.continent != last_continent:
                    if last_continent:
                        if len(continent_indexes) > 0:
                            start_ = continent_indexes[-1][2]
                        else:
                            start_ = 0
                        continent_indexes.append((last_continent, start_, i))
                    last_continent = country.continent
            continent_indexes.append((last_continent, continent_indexes[-1][1], len(countries)))
            return continent_indexes

        with open(self.input_path / self.countries_file, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            countries = []
            for row in skip_comments(reader):
                country = CountryFactory.from_row(row)
                names = self.name_reader.read_names_for(country.geoid, lang)
                country.update(names)
                countries.append(country)
        countries = sorted(countries, key=lambda a: (a.continent, a.name))
        continent_indexes = _generate_continent_indexes(countries)
        folder = self.output_path / lang
        if not folder.exists():
            folder.mkdir()
        with open(folder / f'countries_{lang}.py', 'w') as fp:
            fp.write(rowlist_to_template(vars(countries[0]), countries, _continent_indexes=continent_indexes))

    def generate_cities(self, file, lang):
        cities = {}
        timezones = []
        states = self.read_admin_codes(self.states_file, lang)
        districts = self.read_admin_codes(self.districts_file, lang)
        template_keys = None
        with open(self.input_path / file, 'r') as fp:
            reader = csv.reader(fp, delimiter='\t')
            for row in skip_comments(reader):
                city = CityFactory.from_row(row)
                if city.timezone not in timezones:
                    timezones.append(city.timezone)
                names = self.name_reader.read_names_for(city.geoid, lang)
                city.update(names)
                if city.country_code not in cities:
                    cities[city.country_code] = []
                cities[city.country_code].append(city)
                if not template_keys:
                    template_keys = vars(city)
        self.timezone_names = sorted(timezones)
        codes = self.read_country_codes(self.countries_file)
        for code in codes:
            city_list = cities[code] if code in cities else []
            for city in city_list:
                city.timezone = self.timezone_names.index(city.timezone)
            with open(self.output_path / lang / f'{code}_{lang}.py', 'w') as fp:
                fp.write(rowlist_to_template(template_keys, city_list,
                                    _states=self.dump_admincodes(states[code]) if code in states else {},
                                    _districts=self.dump_admincodes(districts[code]) if code in districts else {}))

    def generate_values(self, city_file: str, languages: Iterable[str], default_language):
        self.generate_package()
        self.name_reader.ensure_names()
        for lang in languages:
            self.generate_countries(lang)
            self.generate_cities(city_file, lang)
        write_constants(self.output_path / 'constants.py', default_language, languages, self.timezone_names)

if __name__ == '__main__':
    Generator('../data', 'src/plaincities/_values').generate_values('cities15000.txt', ['ar', 'en', 'zh', 'fr', 'es', 'tr'], 'en')
