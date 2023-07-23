#Importations
import re
import pandas as pd

def clean_text(text):
    '''Fonction de nettoyage d'une chaîne de caractères quelconque.
    Revoie : str'''
    text = re.sub(r'@[a-zA-Z0-9éèà_]+', '', text) #Suppression des identifications
    text = re.sub(r'RT[\s]:+', '', text) #Suppression de la mention RT
    text = re.sub(r'#[a-zA-Z0-9éèa]+', '', text) #Suppression des hashtags
    text = re.sub(r'https?:\/\/\S+', '', text) #Suppression des liens hypertexte
    text = re.sub(r'\n', '', text )
    """text = re.sub(emoj, '', text) #Suppression des emoji"""
    return text

def clean_data(data):
    '''Fonction qui applique le nettoyage textuel sur tous les tweets.
    Renvoie : DataFrame'''
    data_clean = pd.DataFrame(columns=['text'])
    data_clean['text'] = data['text'].apply(clean_text)
    return data_clean

