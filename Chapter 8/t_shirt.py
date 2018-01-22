# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 04:16:44 2017

@author: Ayami
"""

#Assignment 8.3, 8.4: T-Shirt + Large Shirts
def make_shirt(shirt_size = 'L', shirt_message = 'i love python'):
    """Summarises the T-Shirt Size and Message to be printed on it."""
    print("The shirt size should be a " + shirt_size.upper() + " and should say ' " + shirt_message.title() + " '.")

make_shirt()
make_shirt('s', 'jump on the bandwagon !')
make_shirt(shirt_size = 'xl', shirt_message = 'sodapop fanclub')