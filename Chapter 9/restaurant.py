# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 20:16:08 2017

@author: Ayami
"""

#Assignment 9.1: Restaurant, 9.2: Three Restaurants
class Restaurant(object):
    """An attempt to model a restaurant."""
    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Describes what the basic premises of the restaurant."""
        print("\nThere's talk of a new restaurant called " + self.restaurant_name.title() + ".")
        print(self.restaurant_name.title() + " will be serving " + self.cuisine_type.title() + " foods .")
        
    def open_restaurant(self):
        """Indicates that the restaurant is opened."""
        print(self.restaurant_name.title() + " is now opened !")
        
restaurant = Restaurant('sukiya', 'japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()

another_restaurant = Restaurant('melonpans', 'bakery')
another_restaurant.describe_restaurant()

yet_another_restaurant = Restaurant('mochi lava', 'barbeque')
yet_another_restaurant.describe_restaurant()
