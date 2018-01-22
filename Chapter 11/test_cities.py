# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 18:35:54 2018

@author: Ayami
"""

import unittest
from city_country import get_city_country

class CitiesTestCase(unittest.TestCase):
    """tests for 'city_country.py'"""
    
    def test_city_country(self):
        """Does a pair like 'Paris, France' work ?"""
        formatted_city_country = get_city_country('paris', 'france')
        self.assertEqual(formatted_city_country, 'Paris, France')
        
    def test_city_country_population(self):
        """Expected output: 'Paris, France - population: 2210000' """
        formatted_city_country_population = get_city_country('paris', 'france', 2210000)
        self.assertEqual(formatted_city_country_population, 'Paris, France - population 2210000')
        
unittest.main()
