# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 18:29:46 2018

@author: Ayami
"""

def get_city_country(city, country, population = ''):
    """generate a neatly formatted city, country pair"""
    if population:
        city_country = city.title() + ', ' + country.title() + ' - population ' + str(population)
        return city_country
    else:
        city_country = city + ', ' + country
        return city_country.title()
