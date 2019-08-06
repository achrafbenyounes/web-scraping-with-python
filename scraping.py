from time import sleep
from time import time
from random import randint
from IPython.display import clear_output
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

#Paginer sur le site jusqu'à 4 pages, use comprehension list to create a list of strings containing the page number
pages = [str(i) for i in range(1,5)]

#Chercher les films entre 2017 et 2018
years_url = [str(i) for i in range(2000, 2018)]

#On fixe la date de début du script
start_time = time()

#Variable qui calcule le nombre de requête
requests = 0

# Pour chaque année entre 2000 et 2017
for year_url in years_url:
    #Pour chaque page entre 1 et 4
    for page in pages:
        # Faire une requête GET sur le site imdb
        response = get('https://www.imdb.com/search/title/?release_date='+year_url + '&sort=num_votes,desc&page='+ page +'')
        # Pause la boucle de 8 à 15 secondes
        sleep(randint(8, 15))
        #Afficher les informations sur les requêtes
        request += 1 # Il s'agit d'une nouvelle requête, on incrémente par 1
        sleep(randint(1, 3)) # On fait une pause de 1 à 3 secondes
        elapsed_time = time() - start_time # On calcule le temps écoulé depuis la première requête
        print("Requests{}; Frequency{} requests/s".format(request, request/elapsed_time))
        clear_output(wait = True)
        
        #Si le status code est différent de 200, il y a un problème et il faut avertir
        if response.status_code != 200:
            warn('Request:{}; status_code:{}'.format(request, response.status_code))

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

