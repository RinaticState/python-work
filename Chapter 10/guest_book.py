# -*- coding: utf-8 -*-
"""
Created on Sun Jan 07 12:21:47 2018

@author: Ayami
"""

filename = 'guest_book.txt'

def add_to_guestlist(guest_name):
    """adds the user's name to the guestlist"""
    if guest_name != 'q':
        with open(filename, 'a') as file_object:
            file_object.write("\n" + guest_name.title().strip())

print("Enter 'q' to quit")        
while True:
    guest_name = raw_input("Please enter your name: ")
    add_to_guestlist(guest_name = guest_name)
    if guest_name == 'q':
        break
    else:
        print("Top of the day, " + guest_name.title() + " !")
    