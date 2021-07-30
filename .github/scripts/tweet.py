from os import environ
import sys
import tweepy

reload(sys)
sys.setdefaultencoding('utf8')

twitter_key = environ.get("TWITTER_KEY")
twitter_token = environ.get("TWITTER_TOKEN")
access_token = environ.get("ACCESS_TOKEN")
access_secret = environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(twitter_key, twitter_token)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
api.update_status("hello world")
