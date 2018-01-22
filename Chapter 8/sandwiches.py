# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:31:14 2017

@author: Ayami
"""

#Assignment 8.12: Sandwiches
def sandwich_order(name, *toppings):
    """Provides a summary of the desired sandwich order."""
    print("\n" + name.title() + " wants a sandwich with the following: ")
    for topping in toppings:
        print("- " + topping)
        
sandwich_order('rina', 'melted cheese', 'shrimp', 'kewpie')
sandwich_order('alice', 'peppers', 'salmon', 'cream cheese')
sandwich_order('blakely', 'lobster', 'lecctuce', 'spinach')
