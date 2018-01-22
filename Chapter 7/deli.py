# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 14:07:38 2017

@author: Ayami
"""
#Assignment 7.8, 7.9: Deli + No Pastami
sandwich_orders = ['pastrami', 'tuna', 'turkey', 'pastrami', 'ham and cheese', 'chicken', 'pastrami', 'bologna']
finished_sandwiches = []

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print("\nUnfortunately, the deli has run out of pastrami.")

while sandwich_orders:
    sandwich_progress = sandwich_orders.pop()
    print("I made your " + sandwich_progress + " sandwich.")
    finished_sandwiches.append(sandwich_progress)
    
print("\nThe following sandwiches have been made: ")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
