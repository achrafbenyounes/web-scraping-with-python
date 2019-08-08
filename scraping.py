from time import sleep
from time import time
from random import randint
from IPython.display import clear_output
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

# Use pagination to navigate(until 4 pages), use comprehension list to create a list of strings containing the page number
pages = [str(i) for i in range(1,5)]

# Searche the movies between 2017 and 2018
years_url = [str(i) for i in range(2000, 2018)]

# Fix the date at starting script
start_time = time()

# Variable which calculates the request number
requests = 0

# For every year between 2000 and 2017
for year_url in years_url:
    # For every page between 1 et 4
    for page in pages:
        # Do a http GET sur le site imdb
        response = get('https://www.imdb.com/search/title/?release_date='+year_url + '&sort=num_votes,desc&page='+ page +'')
        # Pause the loop between 8 until 15 secondes
        sleep(randint(8, 15))
        # Display request data
        request += 1 # new request, we increment this variable by 1
        sleep(randint(1, 3)) # Do a wait between 1 and 3 secondes
        elapsed_time = time() - start_time # Calculate elapsed time since the first request
        print("Requests{}; Frequency{} requests/s".format(request, request/elapsed_time))
        clear_output(wait = True)
        
        # If the status code is different from 200, there is a problem, we must warning that
        if response.status_code != 200:
            warn('Request:{}; status_code:{}'.format(request, response.status_code))

        #The BeautifulSoup module allow to analyse a html document by gettings and parsing its elements
        html_soup = BeautifulSoup(response.text, 'html.parser')
        movies_container = html_soup .find_all('div', class_="lister-item mode-advanced")

        # Create empty lists containg all the necessary data
        names = []
        years = []
        imdb_ratings = []
        meta_scores = []
        votes = []

        # We base on movies_container for dat extraction

        for container in movies_container:
    
            # if the movies has a metascore, we scrap this information
            if container.find('div', class_="ratings-metascore") is not None:
                # Scrap the movie name
                name = container.h3.a.text
                names.append(name) # We add every movie to the list
        
                # Scrap the movie's year
                year = container.h3.find('span', class_='lister-item-year text-muted unbold').get_text()
                years.append(year) # On ajouter l'année de sortie de film
        
                # Scrap the imdb note
                imdb_rating = float(container.strong.text)
                imdb_ratings.append(imdb_rating)
        
                # Scrap the metascore
                meta_score = container.find('div', class_='inline-block ratings-metascore').span.get_text()
                meta_scores.append(int(meta_score))
            
                # Scrap the nb votes
                vote = container.find('span', attrs={"name":"nv"})['data-value']
                votes.append(int(vote))


data_movies = pd.DataFrame ({
    "movie": names,
    "year": years,
    "imdb_ratings": imdb_ratings,
    "meta_scores": meta_scores,
    "votes": votes
    
})

print("Data visualisation :" )
print(data_movies)

