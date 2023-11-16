import setuptools
from distutils.core import setup

setup(
  name='plaincities',
  packages=['plaincities'],
  version='0.3',
  license='MIT',
  description='A library of places in many languages.',
  author='Ufuk Kocolu',
  author_email='ufuk.kocolu@proton.me',      
  url='https://github.com/ufukk/plaincities',   
  download_url='https://github.com/ufukk/plaincities/archives/latest.tar.gz',
  keywords=['locations', 'cities', 'places'],
  install_requires=[],

  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
  ],
)