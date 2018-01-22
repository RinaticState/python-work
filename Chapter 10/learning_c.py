# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 00:03:55 2018

@author: Ayami
"""

filename = 'learning_python.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C'))
        