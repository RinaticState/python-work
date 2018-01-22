# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 20:58:45 2017

@author: Ayami
"""

#Assignment 8.16: Imports
import city_names_functions
pair = city_names_functions.city_country('riga', 'latvia')
print(pair)

from city_names_functions import city_country
pair = city_country('nagoya', 'japan')
print(pair)

from city_names_functions import city_country as cc
pair = cc('berlin', 'germany')
print(pair)

import city_names_functions as cn
pair = cn.city_country('moscow', 'russia')
print(pair)

from city_names_functions import *
pair = city_country('hanoi', 'vietnam')
print(pair)
