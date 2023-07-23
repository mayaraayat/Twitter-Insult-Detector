import tweepy
from credentials import *

class StdOutListener(tweepy.StreamingClient):
    '''
    Création d'une classe héritant de StreamingClient 
    et faisant appel au CallBack on_tweet afin de spécifier
    le format sous lequel les tweets sont récupérés + ajout 
    d'un retour d'erreur HTTP 420
    '''

    def on_tweet(self, tweet):
        print(f"{tweet.id} {tweet.created_at} ({tweet.author_id}): {tweet.text}")
        print("-"*50) #Séparateur de tweets

    def on_error(self, status):
        if str(status) == "420":
            print(status)
            print(
                "You exceed a limited number of attempts to connect to the streaming API")
            return False
        else:
            return True

def get_rule(queries:list, user_id:int):
    '''
    Fonction générant une règle de Streaming à partir
    d'une liste de mots-clés/hashtags et d'un id utilisateur
    (permettant de streamer les réponses à cet utilisateur).
    Renvoie : str
    '''
    rule = ''
    for i in range(len(queries)):
        rule += (queries[i] + 'OR ')
    rule += ('to:' + str(user_id))
    return rule

def collect_by_streaming_rule(rules:str):
    '''
    Fonction créant un stream à partir
    d'une règle spécifiée.
    Renvoie : None
    '''
    stream = StdOutListener(BEARER_TOKEN) #Création du Stream

    #Nettoyage des règles pré-existantes (les règles sont stateful)
    rule_ids = []
    result = stream.get_rules()
    if result.data != None :
        for rule in result.data:
            print(f"rule marked to delete: {rule.id} - {rule.value}")
            rule_ids.append(rule.id)
    
        if (len(rule_ids) > 0):
            stream.delete_rules(rule_ids)
            stream = StdOutListener(BEARER_TOKEN)

    #Ajout d'une nouvelle règle
    stream.add_rules(tweepy.StreamRule(rules))
    print("New rule added")

    #Affichage
    stream.filter(expansions="author_id", tweet_fields="created_at")
