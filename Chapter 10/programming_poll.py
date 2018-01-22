# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 12:47:32 2018

@author: Ayami
"""

filename = 'programming_poll.txt'

print("Enter 'q' to quit")
while True:
    responses = raw_input("Why do you like programming ? ")
    if responses == 'q':
        break
    else:
        with open(filename, 'a') as file_object:
            file_object.write("\n" + responses)
