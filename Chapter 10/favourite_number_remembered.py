# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 13:06:39 2018

@author: Ayami
"""

import json

def get_favourite_number():
    '''attempts to open the file'''
    filename = 'favourite_number.json'
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
    except ValueError:
        store_favourite_number()
    else:
        print("I know your favourite number ! It is " + number + ".")
            
def store_favourite_number():
    '''stores the user's favourite number'''
    user_number = raw_input("What is your favourite number ? ")
    filename = 'favourite_number.json'
    with open(filename, 'w') as file_object:
        json.dump(user_number, file_object)
    print("We'll remember your favourite number next time.")
    
get_favourite_number()
