# -*- coding: utf-8 -*-
"""
Created on Sat Jan 06 23:31:46 2018

@author: Ayami
"""

filename = 'learning_python.txt'

with open(filename) as file_object:
#    for line in file_object:
#        print(line.strip())
#    contents = file_object.read()
#    print(contents)
    lines = file_object.readlines()
    
for line in lines:
    print(line.strip())