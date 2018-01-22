# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 00:54:31 2018

@author: Ayami
"""

file_cats = 'cats.txt'
file_dogs = 'dogs.txt'

try:
    with open(file_cats) as cats_object:
        cat_lines = cats_object.readlines()

except IOError:
    pass 

else:
    print("Cat Names:")    
    for cat_line in cat_lines:
        print(cat_line)

try:    
    with open(file_dogs) as dogs_object:
        dog_lines = dogs_object.readlines()

except IOError:
    pass

else:
    print("\nDog Names:")    
    for dog_lines in dog_lines:
        print(dog_lines)
