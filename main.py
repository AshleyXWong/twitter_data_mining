# -*- coding: utf-8 -*-
import tweepy
from textblob import TextBlob


consumer_key = 'CENSORED PRIVATE INFORMATION'
consumer_secret = 'CENSORED PRIVATE INFORMATION'
access_token = 'CENSORED PRIVATE INFORMATION'
access_token_secret = 'CENSORED PRIVATE INFORMATION'


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('topoli')

d = {}

for tweet in public_tweets:
    analysis_text = TextBlob(tweet.text)
    sentiment_subj = analysis_text.sentiment.subjectivity
    sentiment_polar = analysis_text.sentiment.polarity

    d[analysis_text] = (sentiment_polar, sentiment_subj)
    #print(tweet.text + str(analysis_text.sentiment) + "\n")
    #print(tweet.text + str(analysis_text.sentiment.polarity) + "\n")


'''
From your own account, create a tweet saying "Hello, world!"

tweet = 'Hello, world!'
api.update_status(status=tweet) 
'''

'''
Testing sentiment analysis TextBlob on a given String

from textblob import TextBlob

wiki = TextBlob("Siraj is angry that he does not get good matches on Tindr")
wiki.tags
'''
