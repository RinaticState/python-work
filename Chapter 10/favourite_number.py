# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:57:20 2018

@author: Ayami
"""

import json

user_numbers = raw_input("What is your favourite number ? ")

filename = 'favourite_number.json'
with open(filename, 'w') as file_object:
    json.dump(user_numbers, file_object)
    