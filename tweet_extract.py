#!/usr/bin/env python
# encoding: utf-8

import tweepy #https://github.com/tweepy/tweepy
import csv

#Twitter API credentials
consumer_key = "FgiLn9hUtiXdY5hwalXV7fLBX"
consumer_secret = "6gQNiPAILfh0opQw0py6nT59OSI9du0AkoPmGsdpGv9necrDtN"
access_key = "151838493-nGoW2oIyFqQokv0cinwzNtGyqTqAaWpd2qT06qaN"
access_secret = "hMxTCULa7Cjm2NcUgLLj4TDccpodAs4pZmOrrnEHfmqgk"

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

for status in tweepy.Cursor(api.user_timeline, screen_name='@CNN', tweet_mode="extended").items():
    print(status.full_text)
    print(status.created_at)
    print(status.favorite_count)
    print(status.retweet_count)
    print(status.id_str)
    
#def get_all_tweets(screen_name):
#    #Twitter only allows access to a users most recent 3240 tweets with this method
#
#    #authorize twitter, initialize tweepy
#    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
#    auth.set_access_token(access_key, access_secret)
#    api = tweepy.API(auth)
#
#    #initialize a list to hold all the tweepy Tweets
#    alltweets = []  
#
#    #make initial request for most recent tweets (200 is the maximum allowed count)
#    new_tweets = api.user_timeline(screen_name = screen_name)
#
#    #save most recent tweets
#    alltweets.extend(new_tweets)
#
#    #save the id of the oldest tweet less one
#    oldest = alltweets[-1].id - 1
#
#    #keep grabbing tweets until there are no tweets left to grab
#    while len(new_tweets) > 0:
#        print ("getting tweets before %s" % (oldest))
#
#        #all subsiquent requests use the max_id param to prevent duplicates
#        new_tweets = api.user_timeline(screen_name = screen_name,max_id=oldest)
#
#        #save most recent tweets
#        alltweets.extend(new_tweets)
#
#        #update the id of the oldest tweet less one
#        oldest = alltweets[-1].id - 1
#
#        print ("...%s tweets downloaded so far" % (len(alltweets)))
#
#    #transform the tweepy tweets into a 2D array that will populate the csv 
#    outtweets = [[tweet.id_str, tweet.created_at, tweet.favorite_count, tweet.retweet_count, tweet.full_text] for tweet in alltweets]
#
#    #write the csv  
#    with open('%s_tweets.csv' % screen_name, 'w') as f:
#        writer = csv.writer(f)
#        writer.writerow(["id","Favourite", "retweet", "created_at","text"])
#        writer.writerows(outtweets)
#
#    pass
#
#
#if __name__ == '__main__':
#    #pass in the username of the account you want to download
#    get_all_tweets("CNN")