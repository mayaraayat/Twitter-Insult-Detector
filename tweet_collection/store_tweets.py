#Importations
import re
import json
import pandas as pd

def tweets_to_json(tweets, filename):
    '''
    Crée un fichier json à partir de tweets.
    '''
    d = {}
    d['id'] = [tweet.id for tweet in tweets]
    d['text'] = [tweet.text for tweet in tweets]
    d['date'] = [tweet.created_at.strftime('%d/%m/%y') for tweet in tweets]
    d['hashtags'] = [re.findall(r'#[\S]+', tweet.text) for tweet in tweets]
    d['mentions'] = [re.findall(r'@[\S]+', tweet.text) for tweet in tweets]
    d['Likes'] = [tweet.favorite_count for tweet in tweets]
    d['RTs'] = [tweet.retweet_count for tweet in tweets]
    with open(filename + '.json', 'w', encoding='utf-8') as f:
        json.dump(d, f, indent=4)

def tweets_to_pandas(tweets):
    '''
    Crée un dataframe pandas à partir de tweets.
    '''
    d = {}
    d['id'] = [tweet.id for tweet in tweets]
    d['text'] = [tweet.text for tweet in tweets]
    d['date'] = [tweet.created_at.strftime('%d/%m/%y') for tweet in tweets]
    d['hashtags'] = [re.findall(r'#[\S]+', tweet.text) for tweet in tweets]
    d['mentions'] = [re.findall(r'@[\S]+', tweet.text) for tweet in tweets]
    d['Likes'] = [tweet.favorite_count for tweet in tweets]
    d['RTs'] = [tweet.retweet_count for tweet in tweets]
    data = pd.DataFrame.from_dict(d)
    return data

    

