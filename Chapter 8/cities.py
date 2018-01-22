# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 04:26:03 2017

@author: Ayami
"""

#Assignment 8.5: Cities
def describe_city(city_name, country_name = 'vietnam'):
    """Prints the city name associated with the country."""
    print(city_name.title() + " is in " + country_name.title() + ".")

describe_city('ho chi minh city')
describe_city('da nang')
describe_city('nha trang')
describe_city(city_name = 'nagoya', country_name = 'japan')
