# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 13:03:38 2018

@author: Ayami
"""

import json

filename = 'favourite_number.json'
with open(filename) as file_object:
    user_number = json.load(file_object)
    
print("I know your favourite number ! It's " + user_number + ".")
