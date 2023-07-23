#Importations
import re
import tweepy


def get_queries(dir_path:str, query_id:int):
    '''
    Récupère une liste de requêtes à partir de deux fichiers 
    contenant respectivement mots-clés et hashtags à rechercher.
    file_path : chemin du dossier contenant les fichiers
    query_id : numéro associé aux fichiers
    Renvoie : liste de requêtes (str)
    '''
    try:
        with open(dir_path+'keywords_'+str(query_id)+'.txt') as key:
            keys = key.readlines()
        with open(dir_path+'hashtag_'+str(query_id)+'.txt') as hash:
            hashtags = hash.readlines() 
        L = []
        for i in keys:
            L += re.split(r';', i)
        for i in hashtags:
            L += re.split(r';', i)
        return list(set(L))
    except IOError:
        raise KeyError
    

def get_tweets_from_search(queries:list, twitter_api:tweepy.API):
    '''
    Recherche les tweets correspondant à une liste de requêtes
    queries : liste de requêtes
    twitter_api : connexion à l'api Twitter
    Renvoie : liste de SearchResults
    '''
    try:
        return [twitter_api.search_tweets(i) for i in queries]
    except tweepy.TweepyException:
        raise KeyError

def condition_search(cond:dict, twitter_api:tweepy.API):
    '''
    Effectue une recherche à partir de conditions
    cond : dictionnaire d'arguments de search_tweets et valeurs
    twitter_api : connexion à l'api Twitter
    Renvoie : SearchResults
    '''
    return twitter_api.search_tweets(**cond)




