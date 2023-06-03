# -*- coding: utf-8 -*-
import re
import rake
import json

class TwitterClient(object):
    def clean_tweet(self, tweet):
        #import PreProcessing
        #PreProcessing.preProcess(tweet)
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweets(self):
        tweets = []
        privacy_count = 0
        tweets_file = open('twitter_data.txt', "r", encoding='cp1252')
        for tweet in tweets_file:
            tweet = json.loads(tweet)
            is_privacy = rake.Rake(tweet)
            if is_privacy:
                print("is_privacy :", is_privacy)
                privacy_count += 1
            else:
                print("is_privacy :", is_privacy)
                print("==== "*10)
            tweets.append(tweet)
        return tweets	

def main():
    # creating object of TwitterClient Class
    api = TwitterClient()
    # calling function to get tweets
    tweets = api.get_tweets()

if __name__ == "__main__":
    # calling main function
    main()
