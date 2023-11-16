import pytest

def test_country_select():
    from plaincities import Countries

    countries = Countries()

    assert 'Yemen' in countries
    assert 'Vietnam' in countries
    assert 'Cuba' in countries

    assert(countries['Cuba'].alpha2 == 'CU')
    assert(countries['Cuba'].alpha3 == 'CUB')
    assert(countries['Cuba'].fips == 192)
    assert(countries['Vietnam'].alpha3 == 'VNM')
    assert(countries['Yemen'].fips == 887)
    assert(countries['VNM'].name == 'Vietnam')
    assert(countries['CU'].alpha3 == 'CUB')

    assert(countries['Djibouti'].continent == 'AF')
    assert(countries['Cuba'].continent == 'NA')
    assert(countries['Dominican Republic'].continent == 'NA')
    assert(countries['India'].continent == 'AS')

def test_state_select():
    from plaincities import Countries
    countries = Countries()
    countries['IN'].load_cities()
    countries['CN'].load_cities()
    countries['IQ'].load_cities()
    countries['IR'].load_cities()
    countries['MX'].load_cities()
    assert 'Texas' not in countries['IN'].states
    assert 'Kerala' in countries['IN'].states
    assert 'Xinjiang' in countries['CN'].states
    assert 'Basra' in countries['IQ'].states
    assert 'Fars' in countries['IR'].states
    assert 'Yucatan'in countries['MX'].states

def test_city_select():
    from plaincities import Countries
    countries = Countries()
    germany = countries['DE']
    germany.load_cities()
    assert 'Cologne District' in germany.states['North Rhine-Westphalia'].districts
    assert len(germany.states['North Rhine-Westphalia'].\
        districts['Cologne District'].cities) > 0
    koln = germany.states['North Rhine-Westphalia']\
        .districts['Cologne District'].cities['Cologne']
    assert koln.name == 'Cologne'
    turkiye = countries['TR']
    turkiye.load_cities()
    assert 'Ankara' in turkiye.states
    assert 'Ankara' in turkiye.cities
    ankara_city = turkiye.cities['Ankara']
    assert(ankara_city.timezone.key == 'Europe/Istanbul')
    iraq = countries['IQ']
    iraq.load_cities()
    assert 'Baghdad' in iraq.cities

def test_countries_load_options():
    from plaincities import Countries
    countries = Countries(countries_to_load=['IN'])
    assert 'Kerala' in countries['IN'].states
    countries = Countries(continents_to_load=['AF'])
    assert 'Eastern Cape' in countries['ZA'].states
    countries = Countries(load_all=True)
    assert 'Bağcılar' in countries['TR'].states['Istanbul'].cities
    assert 'Bagcilar' in countries['TR'].states['Istanbul'].cities

def test_city_properties():
    from plaincities import Countries
    countries = Countries(countries_to_load=['CN', 'RU'])
    china = countries['CN']
    guangzhou = china.cities['Guangzhou']
    xining = china.cities['Xining']
    assert guangzhou.latitude < xining.latitude
    assert guangzhou.longitude > xining.longitude
    russia = countries['RU']
    kaliningrad = russia.cities['Kaliningrad']
    moscow = russia.cities['Moscow']
    assert moscow.population > 1000000
    assert moscow.population > kaliningrad.population

def test_city_name_suggestions():
    from plaincities import Countries
    countries = Countries(countries_to_load=['TR', 'GR'])
    turkiye = countries['TR']
    greece = countries['GR']
    ankara_suggestions = list(turkiye.cities.suggest('nkara'))
    assert 'Ankara' in ankara_suggestions
    thessaloniki_suggestions = list(greece.cities.suggest('Tesaloniki'))
    assert 'Thessaloniki' in thessaloniki_suggestions

def test_filters():
    from plaincities import Countries
    countries = Countries(countries_to_load=['CU'])
    cuba = countries['CU']
    large_cities = cuba.cities.filter(lambda x: x.population > 100000)
    assert cuba.cities['Havana'] in large_cities

def test_languages():
    from plaincities import Countries
    countries = Countries(language='zh', countries_to_load=['CN'])
    china = countries['CN']
    assert china.name == '中国'
    assert '北京' in china.cities
    countries = Countries(language='tr', countries_to_load=['DE'])
    germany = countries['DE']
    assert germany.name == 'Almanya'
    assert 'Berlin' in germany.cities
    assert 'Münih' in germany.cities
    countries = Countries(language='ar', countries_to_load=['LB'])
    lebanon = countries['LB']
    assert lebanon.name == 'لبنان'
    assert 'بيروت' in lebanon.cities

