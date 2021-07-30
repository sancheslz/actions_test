# -*- coding: utf-8 -*-

from os import environ
import tweepy

twitter_token = environ.get("TWITTER_TOKEN")
twitter_key = environ.get("TWITTER_KEY")
access_token = environ.get("ACCESS_TOKEN")
access_secret = environ.get("ACCESS_SECRET")

auth = tweepy.OAuthHandler(twitter_key, twitter_token)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)
api.update_status('{actor} ({action}): {message}'.format(
    actor=environ.get('actor'),
    action=environ.get('action'),
    message=environ.get('message')
))
