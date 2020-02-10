#Initial Empty File
import tweepy
import pandas as pd
import os
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
#You will need to import your own Twitter developer credentials
#In order to do it, create a file called "credentials.csv"
#And set it up as follows
# consumer_key,consumer_secret,access_token,access_token_secret

#This code will read in your credentials and then be able
#to run

credentials = list(pd.read_csv(os.getcwd()+'/credentials.csv').columns)

#Authorizes the script based on credentials in the credentials file
auth = tweepy.OAuthHandler(credentials[0],credentials[1])
auth.set_access_token(credentials[2],credentials[3])
#Creates the api object
api = tweepy.API(auth)

#Defines function to create the word cloud
def make_cloud(string):
    cloud = WordCloud(background_color = 'white',
                      max_words = 200,
                      stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file('cloud.png')




topic = "bernie"

#Collects the twelve most popular tweets pertaining to the topic above
#and prints them
popular_tweets = api.search(q=topic, result_type='popular',tweet_mode='extended')

texts = []
text_string = ''
for i in range(len(popular_tweets)):
    texts.append(popular_tweets[i].full_text.lower())
    text_string = text_string+popular_tweets[i].full_text.lower()+' '
    
make_cloud(text_string)