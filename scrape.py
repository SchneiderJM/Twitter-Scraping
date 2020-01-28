#Initial Empty File
import tweepy
import pandas as pd
import os
#You will need to import your own Twitter developer credentials
#In order to do it, create a file called "credentials.csv"
#And set it up as follows
# consumer_key,consumer_secret,access_token,access_token_secret

#This code will read in your credentials and then be able
#to run

credentials = list(pd.read_csv(os.getcwd()+'\\credentials.csv').columns)

#Authorizes the script based on credentials in the credentials file
auth = tweepy.OAuthHandler(credentials[0],credentials[1])
auth.set_access_token(credentials[2],credentials[3])
#Creates the api object
api = tweepy.API(auth)

topic = "shoes"

#Collects the twelve most popular tweets pertaining to the topic above
#and prints them
popular_tweets = api.search(q=topic, result_type='popular')
