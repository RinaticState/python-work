# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 05:09:17 2017

@author: Ayami
"""

#Assignment 8.6: City Names
def city_country(city, country):
    """Returns a neatly formatted city-country pair"""
    city_and_country = city + ', ' + country
    return city_and_country.title()
pair = city_country(city = 'tokyo', country = 'japan')
print(pair)
pair = city_country(city = 'riga', country = 'latvia')
print(pair)
pair = city_country(city = 'moscow', country = 'russia')
print(pair)
