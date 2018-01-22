# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 13:47:42 2018

@author: Ayami
"""

print("Enter 'q' to quit")

while True:
    number_one = raw_input("Enter a number: ")
    if number_one == 'q':
        break
    number_two = raw_input("Enter another number: ")
    if number_two == 'q':
        break
    try:
        addition = int(number_one) + int(number_two)
    except ValueError:
        print("\nPlease enter a number, not text !")
    else:
        print("\nAnswer: " + str(addition))
        