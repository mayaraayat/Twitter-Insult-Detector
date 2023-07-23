import tweepy
from credentials import *

def twitter_setup():
    '''
    Se connecte à l'api Twitter à l'aide
    des données d'authentification.
    '''
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

    #Return API with authentication:
    api = tweepy.API(auth)
    return api

