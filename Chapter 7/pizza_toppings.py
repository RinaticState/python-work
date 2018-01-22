# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 06:34:29 2017

@author: Ayami
"""

# Assignment 7.4: Pizza Toppings

prompt = "\nWhat would you like on your pizza ?"
prompt += "\nEnter 'quit' to exit the program. "

message = " "
while message != 'quit':
    message = raw_input(prompt)
    
    if message != 'quit':
        print(message.title() + " has been added to your pizza !")