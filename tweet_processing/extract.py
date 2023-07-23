#Importations
import pandas as pd

def json_to_text(path:str):
    '''Fonction de récuperation des textes bruts des tweet collectés. 
    Renvoie : DataFrame'''
    file = pd.read_json(path)
    L = [file.get('tweet_textual_content')[i] for i in file.index] 
    return pd.DataFrame(L, columns=['text'])

def dataframe_to_text(df):
    '''
    Récupère le texte de tweets contenus
    un dataframe.
    '''
    L = [df.get('tweet_textual_content')[i] for i in df.index] 
    return pd.DataFrame(L, columns=['text'])

def extract_all(lis, data):
    d = {}
    d['tweet_textual_content'] = []
    d['len'] = []
    d['ID'] = []
    d['Date'] = []
    d['Source'] = []
    d['Likes'] = []
    d['RTs'] = []
    for i in lis:
        for j in d:
            d[j] += [data[j][i]]
    return d

def extract_list(cond, data):
    return data[cond].index