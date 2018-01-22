# -*- coding: utf-8 -*-
"""
Created on Tue Jan 09 12:06:10 2018

@author: Ayami
"""

def find_words(filename):
    try:
        with open(filename) as file_object:
            words = file_object.read()
    except IOError:
        print("Sorry, but the file " + filename + " could not be found.")
    else:
        words_count = words.lower().count('the')
        print(filename + "has " + str(words_count) + " counts of the word 'the' .")
        
filenames = ['this_side_of_paradise.txt', 'uncle_toms_cabin.txt',
             'war_of_the_worlds.txt', 'the_scarlet_letter.txt']
for filename in filenames:
    find_words(filename = filename)