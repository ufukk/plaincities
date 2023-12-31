
plaincities is a library of places in many languages. It is based on `geonames <https://www.geonames.org/>`_ database.


Installation
------------

.. code-block:: text

    pip install plaincities


Usage
-----


Load options:
====================

.. code-block:: python

    from plaincities import Globe
    globe = Globe(load_all=True)
    globe = Globe(continents_to_load=['AF', 'AS'])
    globe = Globe(countries_to_load=['IN', 'MX'])

    globe = Globe()
    india = globe['IN']
    india.load_cities()

Hierarchy & Administrative Divisions:
========================================

.. code-block:: python

    from plaincities import Globe
    globe = Globe(countries_to_load=['MY'])
    malaysia = globe['MY']
    medium_cities = list(malaysia.cities.filter(lambda x: x.population > 100000 and x.population < 1000000 and x.district is not None))['/'.join(
        [c.state.name, c.district.name, c.name, c.admin_division.name])
    for c in medium_cities][0:10]

.. code-block:: text

    ['Johor/Daerah Batu Pahat/Batu Pahat/Place',
 'Johor/Daerah Johor Baharu/Kampung Pasir Gudang Baru/Place',
 'Johor/Daerah Johor Baharu/Skudai/Section',
 'Johor/Daerah Johor Baharu/Johor Bahru/City',
 'Johor/Daerah Keluang/Kluang/Place',
 'Johor/Daerah Muar/Muar town/Place',
 'Selangor/Petaling/Shah Alam/Place',
 'Selangor/Klang/Klang/Place',
 'Sabah/Kota Kinabalu/Kota Kinabalu/City',
 'Sabah/Lahad Datu/Lahad Datu/Place']


Coordinates:
====================

.. code-block:: python

    globe = Globe(countries_to_load=['IN'])
    india = globe['IN']
    kochi = india.cities.find('Kochi')
    (kochi.latitude, kochi.longitude)

.. code-block:: text

    (9.93988, 76.26022)


.. code-block:: python

    globe = Globe(countries_to_load=['IN'])
    india = globe['IN']
    varanasi = india.cities.find('Varanasi')
    new_delhi = india.cities.find('New Delhi')
    f'~{round(varanasi.distance_to(new_delhi) / 1000)} km.' 

.. code-block:: text

    '~682 km.'


Timezones:
====================

.. code-block:: python

    globe = Globe(countries_to_load=['MX'])
    mexico = globe['MX']
    merida = mexico.cities.find('Merida')
    merida.timezone.key

.. code-block:: text

    'America/Merida'



Switching languages:
====================

.. code-block:: python

    from plaincities import Globe
    globe = Globe(language='zh', countries_to_load=['CN'])
    china = globe['CN']
    beijing = china.cities.find('北京')
    (china.name, beijing.name, beijing.ascii_name)

.. code-block:: text

   ('中国', '北京', 'Beijing')

Suggestions:
====================

.. code-block:: python

    from plaincities import Globe
    globe = Globe(countries_to_load=['GR'])
    greece = countries['GR']
    list(greece.cities.suggest('Tesaloniki', threshold=0.7))


.. code-block:: text

   ['Heraklion', 'Thessaloniki']



Generating language files
-------------------------

Default installation supports English, Turkish, French, Spanish, Chinese, Russian and Arabic.
If you need other languages, you need to download the following files from the `geonames website <https://download.geonames.org/export/dump/readme.txt>`_ and put them into the same folder:

    countryInfo.txt, alternateNamesv2.zip, admin1CodesASCII.txt, admin2Codes.txt, cities(N).zip

.. code-block:: python

    from plaincities import generator
    Generator('data', 'new_values').generate_values('cities15000.txt', languages=['ko'], default_language='ko')

.. code-block:: python

    from plaincities import Globe
    globe = Globe(countries_to_load=['TH'], path='new_values')
    thailand = countries['TH']
    thailand.name

.. code-block:: text

   '태국'


Contact:
--------

ufuk.kocolu@proton.me