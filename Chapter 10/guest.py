# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 12:10:01 2018

@author: Ayami
"""

filename = 'guest.txt'

with open(filename, 'w') as file_object:
    guest_name = raw_input("What is your name ? ")
    file_object.write(guest_name.title())
