#Imports

import sys
import os
sys.path.append(os.path.join(os.getcwd(), 'tweet_processing'))
sys.path.append(os.path.join(os.getcwd(), 'tweet_collection'))
sys.path.append(os.path.join(os.getcwd(), 'translator'))
sys.path.append(os.path.join(os.getcwd(), 'user_interface'))
sys.path.append(os.path.join(os.getcwd(), 'insult_detection'))
sys.path.append(os.path.join(os.getcwd(), 'data_vizualisation'))

if True:
    from data_vizualisation.wordcloud import *
    from tweet_processing.vocab_parsing import *
    from tweet_collection.connect import *
    from tweet_collection.user_collect import *
    from tweet_processing.clean import *

def print_user_worldcloud(user_id, count, path):
    api = twitter_setup()
    df = get_timeline(user_id=user_id, twitter_api=api, count=count)
    vocab=extract_tweets_vocab_sep(df)
    makeImage(vocab, path)

if __name__ == '__main__' :
    print_user_worldcloud(1572446416496099329, 200, 'data_vizualisation/wd_images/detective.png')


