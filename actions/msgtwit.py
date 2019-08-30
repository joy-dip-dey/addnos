import sys
import tweepy
from st2common.runners.base_action import Action

class MyAction(Action):

    def run(self, message):
        consumer_key ="up8xB8CBZIjw2BaAxqKHHXVme"
        consumer_secret ="iBAkJ16MiWJZEUcNbvyHAApkd4wC1y37tIKXYLjXKw2ZN2jLSy"
        access_token ="3693272780-xpWm3Ft0Qvq1wH3IJY6F3vYmYlSu7gcKfrXvGHL"
        access_token_secret = "pEJKaaSDkpAdvOAMZEgappkv80egZotLyTZmJaqyHi50T"
        chek = tweepy.OAuthHandler(consumer_key, consumer_secret)
        chek.set_access_token(access_token, access_token_secret)
        api = tweepy.API(chek) 
        api.update_status(status = message)
        return(True)