# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 13:40:04 2018

@author: Ayami
"""

def get_numbers(number_one, number_two):
    try:
        addition = int(number_one) + int(number_two)
    except ValueError:
        print('please enter a number, not text')
    else:    
        print("\nanswer: " + str(addition))
    
number_one = raw_input('enter a number: ')
number_two = raw_input('enter another number: ')
get_numbers(number_one = number_one, number_two = number_two)
