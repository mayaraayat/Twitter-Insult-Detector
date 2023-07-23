#Importations
import tweepy
import pandas as pd
from search import get_tweets_from_search
from streaming import collect_by_streaming_rule

def get_replies(user_id:int, twitter_api:tweepy.API, count:int):
    '''
    Récupère les réponses aux tweets d'un utilisateur
    et les conserve dans un dictionnaire.
    '''
    tweets = twitter_api.user_timeline(user_id=user_id, count=count)
    name = twitter_api.get_user(user_id=user_id).screen_name
    dict_replies = {}
    for tweet in tweets:
        id = tweet.id
        replies = []
        l = get_tweets_from_search({'q': 'to:'+name})
        for i in l:
            if hasattr(i, 'in_reply_to_status_id_str'):
                if (i.in_reply_to_status_id_str == str(id)):
                    replies.append(i)
        dict_replies[str(id)] = replies
    return dict_replies

def get_retweets(user_id:int, twitter_api:tweepy.API, count:int):
    '''
    Récupère les retweets aux tweets d'un utilisateur
    et les conserve dans un dictionnaire.
    '''
    name = twitter_api.get_user(user_id=user_id).screen_name
    tweets = twitter_api.user_timeline(screen_name=name, count=count)
    dict_retweets = {}
    for tweet in tweets:
        id = tweet.id
        l = get_tweets_from_search({'q': 'RT '+name})
        retweets = []
        for i in l:
            if hasattr(i, 'retweeted_status'):
                retweets.append(i)
        dict_retweets[str(id)] = retweets
    return dict_retweets

def get_timeline(user_id:int, twitter_api:tweepy.API, count:int):
    '''
    Récupère les tweets d'un utilisateur.
    '''
    statuses = twitter_api.user_timeline(user_id=user_id, count=count)
    L = [status.text for status in statuses]
    return pd.DataFrame(L, columns=['text'])

def user_streaming(username:str):
    '''
    Streame les tweets d'un utilisateur.
    '''
    collect_by_streaming_rule('from:'+username)



