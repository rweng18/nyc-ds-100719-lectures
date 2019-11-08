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

# %matplotlib inline

with open('data.csv') as f:
    catalogue = csv.DictReader(f)
    top_500 = []
    for row in catalogue:
        top_500.append(row)

    # def search_name(data, name_key, album_name)
    print(search_name(top_500, 'album', 'The Stone Roses'))
    # def search_rank(data, rank_key, album_rank)
    print(search_rank(top_500, 'number', 498))
    # def search_year(data, year_key, album_year)
    print(search_year(top_500, 'year', 1989))
    # def start_end_year(data, year_key, start, end)
    print(start_end_year(top_500, 'year', 1989, 1990))
    # def start_end_rank(data, rank_key, start, end)
    print(start_end_rank(top_500, 'number', 1, 10))
    # def all_titles(data, title_key)
    print(all_titles(top_500, 'album'))
    # def all_artists(data, artist_key)
    print(all_artists(top_500, 'artist'))
    # def most_albums(data, artist_key):
    print(most_albums(top_500, 'artist'))
    # def most_pop_word(data, title_key)
    print(most_pop_word(top_500, 'album'))
    # def album_decades(decade, year_key)
    plt.show(album_decades(top_500, 'year'))
    # def genre_count(data, genre_key)
    plt.show(genre_count(top_500, 'genre'))