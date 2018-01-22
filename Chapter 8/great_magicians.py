# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 07:03:23 2017

@author: Ayami
"""

#Assignment 8.10: Great Magicians
def show_magicians(magicians):
    """Prints names of magicians from a list."""
    for magician in magicians:
        print("Hello, " + magician.title() + ", are you ready for the big show ?")
def make_great(magicians):
    great_magicians = []
    
    while magicians:
        popped_magician = magicians.pop()
        great_magician = popped_magician + " the great"
        great_magicians.append(great_magician)
    
    for great_magician in great_magicians:
        magicians.append(great_magician)
    
    return magicians
magicians = ['houdini', 'copperfield', 'takayama']
great_magicians = make_great(magicians[:])
show_magicians(great_magicians)
show_magicians(magicians)
