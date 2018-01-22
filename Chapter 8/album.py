# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 05:15:39 2017

@author: Ayami
"""

#Assignment 8.7: Album
def make_album(artist_name, album_title, number_tracks = 0):
    """Returns a dictionary of the album and artist"""
    album = {'artist' : artist_name, 
             'album' : album_title,
             }
    if number_tracks:
        album['tracks'] = number_tracks
    return album

production = make_album(artist_name = 'cidergirl', album_title = 'sodapop fanclub 1', number_tracks = '11')
print(production)
production = make_album(artist_name = 't/ssue', album_title = 'i')
print(production)
production = make_album(artist_name = 'akishibu project', album_title = 'midaregami fighting grl')
print(production)
production = make_album(artist_name = "she's", album_title = 'proust to hanataba')
print(production)
