from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#Attribuer l'url de site imdb au variable url
url = "https://www.imdb.com/search/title/?release_date=2017&sort=num_votes,desc&page=1"

response = get(url)

#The BeautifulSoup module allow to analyse a html document by gettings and parsing its elements
html_soup = BeautifulSoup(response.text, 'html.parser')
movies_container = html_soup .find_all('div', class_="lister-item mode-advanced")

# On crée des listes vides contenant toutes nos informations
names = []
years = []
imdb_ratings = []
meta_scores = []
votes = []

# On reprend notre movies_container pour y extraire l'information

for container in movies_container:
    
    # Si le film a une métascore, on l'extrait
    if container.find('div', class_="ratings-metascore") is not None:
        #Extraire nom du film
        name = container.h3.a.text
        names.append(name) # on ajoute chaque nom du film à la liste
        
        #Extraire year de film
        year = container.h3.find('span', class_='lister-item-year text-muted unbold').get_text()
        years.append(year) # On ajouter l'année de sortie de film
        
        #Extraire la note imdb 
        imdb_rating = float(container.strong.text)
        imdb_ratings.append(imdb_rating)
        
        #Extraire le metascore
        meta_score = container.find('div', class_='inline-block ratings-metascore').span.get_text()
        meta_scores.append(int(meta_score))
        
        #Extraire le nombre de votes
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

