import numpy as np
import tweepy
import json
import pandas as pd
from tweepy import OAuthHandler

# credentials  --> put your credentials here
consumer_key = "FWz48dwHP0mqLhSay9Xlz0YXc"
consumer_secret = "lohMfS1JmZ7aU8DrhgzYrFgYyieEKcAEPpKn5UBjuXyIKxgGuZ"
access_token = "1265910520994988032-yLlxXU2eJv4ZyPblbHNyF0cjmVNzi6"
access_token_secret = "LJLYqB1ryzOmvSLO5kp5Pj0uJOtgO6vclNoUE2fQvQivV"

# calling API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def get_data(userid):
	item = api.get_user(userid)

	tweet_count = 0
	data= []
	for status in tweepy.Cursor(api.user_timeline,id=userid).items():
		tweet_count +=1
		if hasattr(status,'text'):
	
			data.append(status.text)
	return (tweet_count,data) 
# if hasattr(status, "entities"):
#         entities = status.entities
#         if "hashtags" in entities:
#           for ent in entities["hashtags"]:
#             if ent is not None:
#               if "text" in ent:
#                 hashtag = ent["text"]
#                 if hashtag is not None:
#                   hashtags.append(hashtag)
   