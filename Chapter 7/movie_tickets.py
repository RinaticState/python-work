# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 06:42:02 2017

@author: Ayami
"""

# Assignment 7.5: Movie Tickets
prompt = "\nHow old are you ?"
prompt += "\nEnter 'quit' to terminate the program. "

while True:
    age = raw_input(prompt)
    if age == 'quit':
        break
    age = int(age)
    
    if age < 3:
        print("Your admission is free !")
    elif age >= 3 and age < 12:
        print("The ticket costs 10$.")
    elif age >= 12:
        print("The ticket costs 15$.")