# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 05:38:21 2017

@author: Ayami
"""

#Assignment 8.8: User Albums
def make_album(artist_name, album_title, number_tracks = 0):
    """Returns a dictionary of the album and artist"""
    album = {'artist' : artist_name, 
             'album' : album_title,
             }
    if number_tracks:
        album['tracks'] = number_tracks
    return album

while True:
    print("\nEnter the following information needed.")
    print("(enter 'q' at anytime to quit)")
    artists_name = raw_input('Artist Name: ')
    if artists_name == 'q':
        break
    albums_title = raw_input('Album Title: ')
    if albums_title == 'q':
        break
    
    production = make_album(artist_name = artists_name, album_title = albums_title)
    print(production)
    
    