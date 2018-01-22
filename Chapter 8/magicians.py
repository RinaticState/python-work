# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 06:57:30 2017

@author: Ayami
"""

#Assignment 8.9: Magicians
def show_magicians(magicians):
    """Prints names of magicians from a list."""
    for magician in magicians:
        print("Hello, " + magician.title() + ", are you ready for the big show ?")
magicians = ['houdini', 'copperfield', 'takayama']
show_magicians(magicians)
