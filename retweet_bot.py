import tweepy
import os
from services import tweepy_auth, retweet_favorites
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_SECRET = os.getenv('ACCESS_SECRET')

api = tweepy_auth(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_SECRET)
retweet_favorites(api, 'daviddobrik')
