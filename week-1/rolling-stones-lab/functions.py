# import csv
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
# %matplotlib inline


###########################################################################
##  SEARCH FUNCTIONS  #####################################################
###########################################################################

#Find by name - Takes in a string that represents the name of an album. 
#Should return a dictionary with the correct album, or return None.
#

def search_name(data, name_key, album_name):
    for album in data:
        if album_name == album[name_key]:
            return album
    return None
    
#Find by rank - Takes in a number that represents the rank in the list of 
#top albums and returns the album with that rank. If there is no album with that 
#rank, it returns None.
#
def search_rank(data, rank_key, album_rank):
    for album in data:
        if album_rank == int(album[rank_key]):
            return album
    return None

# #Find by year - Takes in a number for the year in which an album was 
# #released and returns a list of albums that were released in that year. 
# #If there are no albums released in the given year, it returns an empty list.
# #
def search_year(data, year_key, album_year):
    years_albums = []
    for album in data:
        if album_year == int(album[year_key]):
            years_albums.append(album)
    return years_albums

# #Find by years - Takes in a start year and end year. 
# #Returns a list of all albums that were released on or between the start and 
# #end years. If no albums are found for those years, then an empty list is returned.
def start_end_year(data, year_key, start, end):
    # era_albums = []
    # for year in range(int(start), int(end + 1)):
    #     era_albums.append(search_year(year, data))
    # return era_albums
    return [search_year(data, year_key, year) for year in range(int(start), int(end + 1))]
    
# #Find by ranks - Takes in a start rank and end rank. 
# #Returns a list of albums that are ranked between the start and end ranks. 
# #If no albums are found for those ranks, then an empty list is returned.
def start_end_rank(data, rank_key, start, end):
    # ranks_albums = []
    # for rank in range(int(start), int(end + 1)):
    #     ranks_albums.append(search_rank(rank, data, rank_key))          
    # return ranks_albums
    return [search_rank(data, rank_key, rank) for rank in range(int(start), 
    	                                                        int(end + 1))]


###########################################################################
##  FIND ALL FUNCTIONS  ###################################################
###########################################################################

# ##   All titles - Returns a list of titles for each album.
def all_titles(data, title_key):
    # titles = []
    # for album in data:
    #     titles.append(album['album'])
    # return titles
    return [datum[title_key] for datum in data]

# #    All artists - Returns a list of artist names for each album. 
def all_artists(data, artist_key):
    # artists = []
    # for album in data:
    #     artists.append(album['artist'])
    # return artists
    return [datum[artist_key] for datum in data]

###########################################################################
##  FIND MOST FUNCTIONS  ##################################################
###########################################################################

# #Artists with the most albums - Returns the artist with the highest amount of
# #albums on the list of top albums
# #
def most_albums(data, artist_key):
    total_artist_list = all_artists(data, artist_key)
    unique_artists = dict.fromkeys(sorted(set(total_artist_list)),0)
    
    # creating counts of albums by artist
    for artist in unique_artists:
        unique_artists[artist] = total_artist_list.count(artist)
    
    # finding artist with highest count
    max_albums = max(unique_artists.values())
    max_artists = []
    for artist in unique_artists:
        if unique_artists.get(artist) == max_albums:
            #adds artists if it has the same number as the max
            max_artists.append(artist)
    return max_artists
    

# #Most popular word - Returns the word used most in amongst all album titles
# #
def most_pop_word(data, title_key):
    #use the list of all the album titles
    total_album_titles = all_titles(data, title_key)
    #split the individual albums titles into indiv words
    words = []
    clean_titles = []
    for title in total_album_titles:
        clean_titles.append(title)
        words.extend(title.split())
    
    for word in words:
        #replace , & / with ''
        if word == '&':    
            words.remove('&')
        if word == '/':
            words.remove('/')
        #corner cases end of starts with punct
        #words.replace(word, word.strip('?'))
        
    # make dictionary of unique words
    unique_words = dict.fromkeys(sorted(set(words)),0)

    # get counts of words
    for word in unique_words:
        unique_words[word] = words.count(word)
        
    # find which word is the most common in the list
    max_count = max(unique_words.values())
    max_words =[]
    for word in unique_words:
        if unique_words.get(word) == max_count:
            #adds artists if it has the same number as the max
            max_words.append(word)
    return max_words
    
###########################################################################
##  HISTOGRAM FUNCTIONS  ##################################################
###########################################################################

# #Histogram of albums by decade - Returns a histogram with each decade pointing 
# #to the number of albums released during that decade.
# #
def album_decades(decade, year_key):
    years = []
    #add each album year in our top 500 list to the years list  
    for album in decade:   
        years.append(int(album[year_key]))
    #find the lowest year in the years list 
    start = round(min(years) - 5, -1)
    # include trailing decade and round down
    end = round(max(years) + 5, -1) 
    current_start = start
    current_end = round(start, -1) - 1
#    decades = []
    dec_bins = []
    
    while current_end < end:
#        decades.append(str(current_start) + '-' + str(current_end))
        dec_bins.append(current_start)
        current_start = current_end + 1
        current_end += 10
   
    dec_bins.append(end) # include end of last decade    
    
    return plt.hist(years, edgecolor = 'black', bins = dec_bins)
  
# #Barplot by genre - Returns a barplot with each genre pointing to the number 
# #of albums that are categorized as being in that genre.
def genre_count(data, genre_key):
    genres = []
    clean_genres = []
    for album in data:   
        #add album genre unclean to genres list
        genres.append(album[genre_key])
    
    for genre in genres:
        # seperate each genre by ,
        current_album = genre.split(',')
        clean_album_genres = []
        #we are getting rid of extraneous instances
        for current_genre in current_album:
            current_genre = current_genre.strip()
            current_genre = current_genre.strip('&')
            current_genre = current_genre.strip()
            clean_album_genres.append(current_genre)
        #add all of the clea_album_genres tot he clean_genres list 
        clean_genres.extend(clean_album_genres)
    
    # make dictionary of unique genres
    unique_genres = dict.fromkeys(sorted(set(clean_genres)),0)

    # get counts of words
    for genre in unique_genres:
        unique_genres[genre] = clean_genres.count(genre)
     
    x = unique_genres.keys()
    y = unique_genres.values()
    return plt.bar(x, y, color = 'green') + plt.xticks(rotation=45, ha="right")
    
    
    
    
    