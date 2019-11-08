import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from functions import search_name
from functions import search_rank
from functions import search_year
from functions import start_end_year
from functions import start_end_rank
from functions import all_titles
from functions import all_artists
from functions import most_albums
from functions import most_pop_word
from functions import album_decades
from functions import genre_count

text_file = open('top-500-songs.txt', 'r')
       # read each line of the text file
       # here is where you can print out the lines to your terminal and get an idea
    #for how you might think about re-formatting the data
lines = text_file.readlines()
songs = []
#for each line in the list of lines
for line in lines:
    #remove the \n treat before and after as seperate strings
    song = line.strip('\n')
    #remove the \t from the front and back as seperate strings 
    songs.append(song.split('\t'))

songs_as_dicts = []
for song in songs:
    #create dict keys and assign them the empty song_as_dict dictionary
    song_as_dict = {}
    song_as_dict['rank'] = song[0]
    song_as_dict['name'] = song[1]
    song_as_dict['artist'] = song[2]
    song_as_dict['year'] = song[3]
    songs_as_dicts.append(song_as_dict)
    
# def search_name(data, name_key, album_name)
print(search_name(songs_as_dicts, 'name', 'Imagine'))
# def search_rank(data, rank_key, album_rank)
print(search_rank(songs_as_dicts, 'rank', 463))
# def search_year(data, year_key, album_year)
print(search_year(songs_as_dicts, 'year', 1989))
# def start_end_year(data, year_key, start, end)
print(start_end_year(songs_as_dicts, 'year', 1989, 1990))
# def start_end_rank(data, rank_key, start, end)
print(start_end_rank(songs_as_dicts, 'rank', 1, 10))
# def all_titles(data, title_key)
print(all_titles(songs_as_dicts, 'name'))
# def all_artists(data, artist_key)
print(all_artists(songs_as_dicts, 'artist'))
# def most_albums(data, artist_key):
print(most_albums(songs_as_dicts, 'artist'))
# def most_pop_word(data, title_key)
print(most_pop_word(songs_as_dicts, 'name'))
# def album_decades(decade, year_key)
plt.show(album_decades(songs_as_dicts, 'year'))
# def genre_count(data, genre_key)
# plt.show(genre_count(songs_as_dicts, 'genre'))