# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:19:56 2017

@author: Ayami
"""
#Assignment 7.10: Dream Vacation

responses = {}

while True:
    name = raw_input("\nWhat is your name ? ")
    prompt = raw_input("\nIf you could visit any place in the world, where would you go ? ")
    responses[name] = prompt
    
    repeat = raw_input("Would you like anyone else to take the poll ? (yes/no) ")
    if repeat == 'no':
        break
    
print("\n\tPoll Results:")
for name, prompt in responses.items():
    print(name.title() + "'s dream vacation is in " + prompt.title() + ".")
