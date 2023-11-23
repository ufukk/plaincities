from importlib.util import spec_from_file_location, module_from_spec
from importlib.abc import Loader
from zoneinfo import ZoneInfo
from difflib import SequenceMatcher
import os
from typing import List, Dict, Iterable, Generator, TypeVar, Generic, Callable, Tuple
from math import asin, sin, cos, radians, sqrt
from enum import Enum, StrEnum, auto

__VALUE_PATH__ = os.path.dirname(os.path.abspath(__file__)) + '/_values'

T = TypeVar('T')

def haversine_distance(lat_1, lon_1, lat_2, lon_2):
    R = 6371008.7714
    lat_1 = radians(lat_1)
    lon_1 = radians(lon_1)
    lat_2 = radians(lat_2)
    lon_2 = radians(lon_2)
    return 2 * R * (asin((sin((lat_2 - lat_1) / 2) ** 2 + \
                               cos(lat_1) * cos(lat_2) * \
                               sin((lon_2 - lon_1) / 2) ** 2) ** 0.5))

def _load_value_file(name, path=None):
    path = path or __VALUE_PATH__
    spec = spec_from_file_location(name, f'{path}/{name}.py')
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def module_to_dict(mod, index):
    values = {}
    for key in vars(mod):
        if key.startswith('_'):
            continue
        name = key[0:-5]
        values[name] = getattr(mod, key)[index]
    return values

def _load_constants():
    return _load_value_file('constants')

class Division:

    def __init__(self, code, level, name) -> None:
        self.code = code
        self.level = level
        self.name = name

class ADCode(StrEnum):

    PPL = auto()
    PPLA = auto()
    PPLA2 = auto()
    PPLA3 = auto()
    PPLA4 = auto()
    PPLA5 = auto()
    PPLC = auto()
    PPLH = auto()
    PPLL = auto()
    PPLX = auto()
    PPLQ = auto()
    PPLS = auto()
    PPLG = auto()
    PPLR = auto()
    PPLF = auto()
    PPLW = auto()

class AD(Enum):

    Capital = Division(ADCode.PPLC, 'capital', 'Capital')
    Place = Division(ADCode.PPL, 'ppl', 'Place')
    City = Division(ADCode.PPLA, 'first-order', 'City')
    Town = Division(ADCode.PPLA2, 'second-order', 'Town')
    Village = Division(ADCode.PPLA3, 'third-order', 'Village')
    SmallVillage = Division(ADCode.PPLA4, 'fourth-order', 'Small Village')
    SmallerVillage = Division(ADCode.PPLA5, 'fifth-order', 'Smaller Village')
    Locality = Division(ADCode.PPLL, 'locality', 'Locality')
    Section = Division(ADCode.PPLX, 'section', 'Section')
    HistoricalPlace = Division(ADCode.PPLH, 'historical-place', 'Historical Place')
    AbandonedPlace = Division(ADCode.PPLQ, 'abandoned-place', 'Abandoned Place')
    PopulatedPlace = Division(ADCode.PPLS, 'populated-place', 'Populated Place')
    SeatOfGovernment = Division(ADCode.PPLG, 'seat-of-government', 'Seat of Government')
    ReligiousPlace = Division(ADCode.PPLR, 'religious place', 'Religious Place')
    FarmPlace = Division(ADCode.PPLF, 'farmn-place', 'Farm Place')
    DestroyedPlace = Division(ADCode.PPLW, 'destroyed-place', 'Destroyed Place')

    @classmethod
    def find(cls, code: str):
        for div in AD:
            if div.value.code.value == code.lower():
                return div
        raise KeyError(code)

class NamedItem:

    def __init__(self, geoid, name, ascii_name=None, alternate_names=None) -> None:
        self.geoid = geoid
        self.name = name
        self.ascii_name = ascii_name
        self.alternate_names = alternate_names

    def same(self, obj: "NamedItem"):
        return self.geoid == obj.geoid

class Container(Generic[T]):
    
    def __init__(self, items: Iterable[T]=None) -> None:
        self.__items = items or []

    def _indexes_for(self, name):
        matches = [i for i, x in enumerate(self.items) if x.name == name or x.ascii_name == name or x.alternate_names and name in x.alternate_names]
        return matches

    @property
    def items(self) -> List[T]:
        return self.__items

    def append(self, obj: NamedItem):
        self.items.append(obj)

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return self.items.__iter__()

    def __contains__(self, key: str) -> bool:
        matches = self._indexes_for(key)
        return len(matches) > 0

    def search(self, name):
        indexes = self._indexes_for(name)
        return [self.items[i] for i in indexes]

    def find(self, name):
        try:
            return self.search(name)[0]
        except IndexError:
            return KeyError(name)

    def suggest(self, query, threshold=0.5) -> Generator[str, None, None]:
        for item in self.items:
            ratio = SequenceMatcher(a=query, b=item.name).quick_ratio()
            if ratio >= threshold:
                yield item.name

    def filter(self, func: Callable) -> Generator[T, None, None]:
        return filter(func, self.items)

class KeyedContainer(Container[T]):
    
    def __getitem__(self, key: str):
        indexes = self._indexes_for(key)
        if len(indexes) == 1:
            return self.items[indexes[0]]
        else:
            raise KeyError(key)

class State(NamedItem):

    def __init__(self, geoid, name, ascii_name, alternate_names=[]) -> None:
        super().__init__(geoid, name, ascii_name, alternate_names)
        self.__disticts = KeyedContainer()
        self.__cities = Container()

    @property
    def districts(self) -> KeyedContainer["District"]:
        return self.__disticts

    @property
    def cities(self) -> Container["City"]:
        return self.__cities

class District(NamedItem):

    def __init__(self, geoid, name, ascii_name=None, alternate_names=None) -> None:
        super().__init__(geoid, name, ascii_name, alternate_names)
        self.__state = None
        self.__cities: Container[City] = Container()

    @property
    def state(self) -> State:
        return self.__state
    
    @state.setter
    def state(self, val):
        self.__state = val
    
    @property
    def cities(self) -> Container["City"]:
        return self.__cities

class City(NamedItem):

    def __init__(self, geoid, name, ascii_name, alternate_names, country_code, latitude: float, longitude: float, timezone: ZoneInfo, population: int, altitude: int, dem: int, admin_division:AD=None, state: State=None, district: "District"=None) -> None:
        super().__init__(geoid, name, ascii_name, alternate_names)
        self.latitude = latitude
        self.longitude = longitude
        self.country_code = country_code
        self.dem = dem
        self.state = state
        self.district = district
        self.timezone:ZoneInfo = timezone
        self.population = population
        self.altitude = altitude
        self.admin_division = admin_division

    def coordinates(self) -> Tuple[float, float]:
        return (self.latitude, self.longitude, )

    def distance_to(self, dest: "City"):
        return haversine_distance(self.latitude, self.longitude, dest.latitude, dest.longitude)

class Country(NamedItem, Container):

    def __init__(self, geoid, name, alpha2, alpha3, fips, capital, area_sqm2, population, languages, currency, continent) -> None:
        super().__init__(geoid, name)
        self.alpha2: str = alpha2
        self.alpha3: str = alpha3
        self.fips: int = fips
        self.capital: City = capital
        self.area_sqm2 = area_sqm2
        self.population = population
        self.languages = languages
        self.currency = currency
        self.continent: str = continent
        self.states: KeyedContainer[State] = None
        self.districts: KeyedContainer[District] = None
        self.cities: Container[City] = None

    def load_cities(self, language=None, path=None):
        constants = _load_constants()
        language = language or constants.default_language
        timezone_names = constants.timezone_names
        if self.cities is None:
            self.cities = Container()
            values = _load_value_file(f'{language}/{self.alpha2}_{language}', path)
            states = {}
            districts = {}
            for key, value in values._states.items():
                states[key] = State(value[2], value[0], value[1])
            for key, value in values._districts.items():
                districts[key] = District(value[2], value[0], value[1])
                state_code = key[0:key.rindex('.')]
                districts[key].state = states[state_code]
                states[state_code].districts.append(districts[key])
            for i, _ in enumerate(values.name_list):
                feature_code = values._feature_code_list[i]
                if feature_code in ['STLMT']:
                    continue
                item = module_to_dict(values, i)
                item['ascii_name'] = item['ascii_name'] if item['ascii_name'] != 0 else item['name']
                item['timezone'] = ZoneInfo(timezone_names[values.timezone_list[i]])
                parent_code = values._parent_code_list[i]
                item['state'] = states[parent_code] if parent_code in values._states else None
                item['district'] = districts[parent_code] if parent_code in values._districts else None
                item['admin_division'] = AD.find(feature_code)
                city = City(**item)
                if city.admin_division == AD.Capital:
                    self.capital = city
                self.cities.append(city)
                if city.state:
                    city.state.cities.append(city)
                if city.district:
                    city.district.cities.append(city)
                    if city.district.state:
                        city.district.state.cities.append(city)
            self.states = KeyedContainer(list(states.values()))
            self.districts = KeyedContainer(list(districts.values()))

    def __contains__(self, key: str):
        return key in self.states

class Globe(Container):
    
    def __init__(self, language=None, load_all=False, countries_to_load:Iterable[str]=None, continents_to_load:Iterable[str]=None, path:str=None) -> None:
        constants = _load_constants()
        language = language or constants.default_language
        countries_to_load = countries_to_load or []
        continents_to_load = continents_to_load or []
        self.__instances: Dict[int, Country] = {}
        self.__values = None
        self.__path = path
        self.__load_countries(language, load_all, countries_to_load, continents_to_load)

    def __load_countries(self, language, load_all, countries_to_load, continents_to_load):
        if not self.__values:
            self.__values = _load_value_file(f'{language}/countries_{language}', self.__path)
            for i, _ in enumerate(self.__values.name_list):
                item = module_to_dict(self.__values, i)
                item['continent'] = self.__continent_for(i, self.__values._continent_indexes)
                country = Country(**item)
                self.__instances[i] = country
                if load_all or country.alpha2 in countries_to_load\
                    or country.continent in continents_to_load:
                    country.load_cities(language=language, path=self.__path)

    def __index_for(self, key: str | int) -> int | None:
        if isinstance(key, str):
            if len(key) > 3:
                return self.__values.name_list.index(key)
            if len(key) == 2:
                return self.__values.alpha2_list.index(key)
            if len(key) == 3:
                return self.__values.alpha3_list.index(key)
        if isinstance(key, int):
            return self.__values.fips_list.index(key)

    def __contains__(self, key: str | int):
        try:
            self.__index_for(key)
            return True
        except IndexError:
            return False

    def __continent_for(self, index, continent_indexes):
        for n, s, e in continent_indexes:
            if index >= s and index < e:
                return n 

    def __getitem__(self, key: str | int) -> Country:
        try:
            index = self.__index_for(key)
            return self.__instances[index]
        except IndexError:
            raise KeyError(key)
