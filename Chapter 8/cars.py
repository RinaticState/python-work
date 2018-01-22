# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:44:13 2017

@author: Ayami
"""

#Assignment 8.14: Cars
def make_car(manufacturer, model_name, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model_name
    for key,value in car_info.items():
        car[key] = value
    return car

car = make_car('toyota', 'corolla', year = '2018', price = '23000$')
print(car)
car = make_car('mitsubishi', 'outlander', colour = 'red', four_wheel_drive = True)
print(car)
