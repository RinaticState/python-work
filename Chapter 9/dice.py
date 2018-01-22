# -*- coding: utf-8 -*-
"""
Created on Fri Jan 05 17:50:53 2018

@author: Ayami
"""

from random import randint

class Die(object):
    def __int__(self, sides):
        self.sides = sides
        
    def roll_die(self):
        random_number = randint(1, self.sides)
        return(random_number)
        
dice_6_sides = Die()
dice_6_sides.sides = 6
results = []
for six_rolls in range(10):
    six_rolls = dice_6_sides.roll_die()
    results.append(six_rolls)
    
print(results)

dice_10_sides = Die()
dice_10_sides.sides = 10
results = []
for ten_rolls in range(10):
    ten_rolls = dice_10_sides.roll_die()
    results.append(ten_rolls)
    
print(results)

dice_20_sides = Die()
dice_20_sides.sides = 20
results = []
for twenty_rolls in range(10):
    twenty_rolls = dice_20_sides.roll_die()
    results.append(twenty_rolls)
    
print(results)