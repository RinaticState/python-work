# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 15:04:51 2017

@author: Nghi
"""

active = True
responses = {}
while active:
    name = raw_input("\nWhat is your name ?")
    prompt = raw_input("\nIf you could go anywhere in the world, where would you go ?")
    responses[name] = prompt
    
    repeat = raw_input("\nDo you want someone else to take the poll ? (yes/no)")
    if repeat == 'no':
        active = False
print("\n\tPoll Results:")
for name, prompt in responses.items():
    print(name.title() + " would like to visit " + prompt.title() + ".")