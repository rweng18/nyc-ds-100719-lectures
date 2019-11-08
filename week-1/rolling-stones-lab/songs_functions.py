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

# Returns the name of the artist and album that has the most songs 
# featured on the top 500 songs list
def albumWithMostTopSongs(albums_data, songs_data, tracks_key, songname_key, artist_key, album_key):
    artists_albums = []
    album_titles = all_titles(albums_data, album_key)
    artists = all_artists(albums_data, artist_key)
    titles_artists = dict(zip(album_titles, artists))
    all_albums = dict.fromkeys(album_titles, 0)

    # Creating counts of songs in top 500 by album
    for song in songs_data:
        # print(song[songname_key])
        for album in albums_data:
            # only finds exact matches, cases where songs were remastered
            # corrected by splitting by ' - '
            # not all song titles covered in tracks data? even so some irregularities in song naming
            if (song[songname_key] in album[tracks_key]): # and (song[artist_key] == album[artist_key]):
                # print(song[songname_key])
                all_albums[album[album_key]] += 1
    print(all_albums)

    max_songs = max(all_albums.values())
    for album in all_albums:
        if all_albums.get(album) == max_songs:
            artist = titles_artists[album]
            artists_albums.append({artist_key: artist, album_key: album})

    return artists_albums

# Returns a list with the name of only the albums that have tracks 
# featured on the list of top 500 songs
def albumsWithTopSongs(albums_data, songs_data, tracks_key, songname_key, artist_key, album_key):
    albums = []
    all_albums = dict.fromkeys(all_titles(albums_data, album_key), 0)

    # Creating counts of songs in top 500 by album
    for song in songs_data:
        # print(song[songname_key])
        for album in albums_data:
            # only finds exact matches, cases where songs were remastered
            # corrected by splitting by ' - '
            # not all song titles covered in tracks data? even so some irregularities in song naming
            if (song[songname_key] in album[tracks_key]): # and (song[artist_key] == album[artist_key]):
                all_albums[album[album_key]] += 1

    albums_with_songs = []
    for album in all_albums:
        if all_albums.get(album) != 0:
            albums_with_songs.append(album)
    return albums_with_songs

# Returns a list with the name of only the songs
# featured on the list of top albums
def songsThatAreOnTopAlbums(albums_data, tracks_key):
    top_albums_songs = []
    for album in albums_data:
    	top_albums_songs.extend(album[tracks_key])
    return top_albums_songs

# Returns a histogram with the 10 albums that have the most songs
# that appear in the top songs list. The album names should point
# to the number of songs that appear on the top 500 songs list.
def top10AlbumsByTopSongs(albums_data, songs_data, tracks_key, songname_key, album_key):
    album_titles = all_titles(albums_data, album_key)
    all_albums = dict.fromkeys(album_titles, 0)

    # Creating counts of songs in top 500 by album
    for song in songs_data:
        # print(song[songname_key])
        for album in albums_data:
            # only finds exact matches, cases where songs were remastered
            # corrected by splitting by ' - '
            # not all song titles covered in tracks data? even so some irregularities in song naming
            if (song[songname_key] in album[tracks_key]): # and (song[artist_key] == album[artist_key]):
                # print(song[songname_key])
                all_albums[album[album_key]] += 1

    bar_names = sorted(all_albums, key = all_albums.get, reverse = True)[0:10]
    bar_heights = []
    for name in bar_names:
    	bar_heights.append(all_albums.get(name))
    return plt.bar(bar_names, bar_heights) + plt.xticks(rotation=45, ha="right")

# Artist featured with the most songs and albums on the two lists.
# This means that if Brittany Spears had 3 of her albums featured
# on the top albums listed and 10 of her songs featured on the top
# songs, she would have a total of 13. The artist with the highest
# aggregate score would be the top overall artist.
def topOverallArtist(albums_data, songs_data, artist_key):
    all_artists = [album[artist_key] for album in albums_data]
    all_artists.extend([song[artist_key] for song in songs_data])
    unique_artists = dict.fromkeys(sorted(set(all_artists)), 0)
    top_artists = []

    for artist in unique_artists:
        unique_artists[artist] = all_artists.count(artist)

    max_features = max(unique_artists.values())

    for artist in unique_artists:
        if unique_artists.get(artist) == max_features:
            top_artists.append(artist)

    return top_artists

