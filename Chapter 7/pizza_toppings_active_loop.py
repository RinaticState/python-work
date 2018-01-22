# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 07:06:35 2017

@author: Ayami
"""

prompt = "\nWhat would you like on your pizza ?"
prompt += "\nEnter 'quit' to exit the program. "
active = True
while active:
    topping = raw_input(prompt)
    if topping == 'quit':
        active = False
    else:
        print(topping.title() + " will be added on your pizza !")
        