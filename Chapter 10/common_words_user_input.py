# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:06:10 2018

@author: Ayami
"""

# this is my own twist on the assignment 10.10 where the user could input their desired word.

def find_words(filename, user_input):
    '''finds desired word in textfile'''
    try:
        with open(filename) as file_object:
            words = file_object.read()
    except IOError:
        print("Sorry, but the file " + filename + " could not be found.")
    else:
        word_count = words.lower().count(user_input)
        print("\nThe word " + user_input + " appears " + str(word_count) + " in the file " + filename)
    
filenames = ['this_side_of_paradise.txt', 'uncle_toms_cabin.txt',
             'war_of_the_worlds.txt', 'the_scarlet_letter.txt']
user_input = raw_input("What word would you like to find ? ")
for filename in filenames:
    find_words(filename = filename, user_input = user_input)
    