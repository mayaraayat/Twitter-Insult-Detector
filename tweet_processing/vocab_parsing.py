#Imports
import textblob as tb
from clean import clean_data
from nltk.corpus import stopwords


def extract_tweets_vocab(tweets_df):
    '''
    Fonction d'extraction du vocabulaire pertinent. 
    Crée un dataframe à partir de tweets récoltés,
    récupère le texte et retire les termes spéciaux, 
    puis crée un objet TextBlob permettant d'extraire
    les mots individuels avant de retirer les stop_words
    de toutes les langues supportées.
    Renvoie : liste de mots pertinents
    '''
    clean_text = clean_data(tweets_df)
    string = ''
    for i in clean_text.index:
        string += clean_text['text'][i]
    wiki = tb.TextBlob(string)
    L = wiki.words
    stops = [stopwords.words(i) for i in stopwords.fileids()]
    stops_total = []
    for i in range(len(stops)):
        for j in range(len(stops[i])):
            stops_total.append(stops[i][j])
    vocab = [w for w in L if not w.lower() in stops_total]
    return vocab

def extract_single_tweet_vocab(tweets_df, index):
    '''
    Idem mais pour un seul tweet identifié par son indice
    dans le dataframe. Permet l'analyse tweet par tweet.
    '''
    clean_text = clean_data(tweets_df)
    string = clean_text['text'][index]
    wiki = tb.TextBlob(string)
    L = wiki.words
    stops = [stopwords.words(i) for i in stopwords.fileids()]
    stops_total = []
    for i in range(len(stops)):
        for j in range(len(stops[i])):
            stops_total.append(stops[i][j])
    vocab = [w for w in L if not w.lower() in stops_total]
    return vocab

def extract_tweets_vocab_sep(tweets_df):
    vocab_sep = []
    for i in range(tweets_df.shape[0]):
        vocab_sep.append(extract_single_tweet_vocab(tweets_df, i))
    return vocab_sep