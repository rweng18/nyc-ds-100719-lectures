import json
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
from songs_functions import albumWithMostTopSongs
from songs_functions import albumsWithTopSongs
from songs_functions import songsThatAreOnTopAlbums
from songs_functions import top10AlbumsByTopSongs
from songs_functions import topOverallArtist

# Load file with Top 500 albums and their tracks
file = open('track_data.json', 'r')
albums_with_tracks = json.load(file)

# Load file with Top 500 songs
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

for album in albums_with_tracks:
	clean_tracks = []
	for track in album['tracks']:
		clean_track = track.split('-')
		clean_tracks.append(clean_track[0].strip())
	album['tracks'] = clean_tracks

songs_as_dicts = []
for song in songs:
    #create dict keys and assign them the empty song_as_dict dictionary
    song_as_dict = {}
    song_as_dict['rank'] = song[0]
    song_as_dict['name'] = song[1]
    song_as_dict['artist'] = song[2]
    song_as_dict['year'] = song[3]
    songs_as_dicts.append(song_as_dict)

# def albumWithMostTopSongs(albums_data, songs_data, tracks_key, songname_key, artist_key, album_key)
print(albumWithMostTopSongs(albums_with_tracks, songs_as_dicts, 'tracks', 'name', 'artist', 'album'))

# def albumsWithTopSongs(albums_data, songs_data, tracks_key, songname_key, artist_key, album_key):
print(len(albumsWithTopSongs(albums_with_tracks, songs_as_dicts, 'tracks', 'name', 'artist', 'album')))

# def songsThatAreOnTopAlbums(albums_data, tracks_key)
print(len(songsThatAreOnTopAlbums(albums_with_tracks, 'tracks')))

# def top10AlbumsByTopSongs(albums_data, songs_data, tracks_key, songname_key, album_key)
plt.show(top10AlbumsByTopSongs(albums_with_tracks, songs_as_dicts, 'tracks', 'name', 'album'))

# def topOverallArtist(albums_data, songs_data, artist_key):
print(topOverallArtist(albums_with_tracks, songs_as_dicts, 'artist'))

