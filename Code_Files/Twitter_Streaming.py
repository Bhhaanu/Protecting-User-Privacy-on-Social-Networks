# -*- coding: utf-8 -*-
from tweepy import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "1281942076796485637-GhFJsNUM7wbEJYdPJCPe2Ug2fcr3U9"
access_token_secret = "Pwybdg2fC1oddODv9i6WjmWFdzOOEPZTf69PguyOS"
consumer_key = "OeuM5VDa9fJuLWTT3ktuTnM1n"
consumer_secret = "WsBUWXEE3tPCTxOTLuUDZGMeEV6UxT5BtFvH7bIJT"

filewriter = open("twitter_data.txt", 'w')
i = 1
# no of tweets need to load
no_tweets = 5
lines = []

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):
    def on_data(self, data):
        global i
        global no_tweets
        if i > no_tweets:
            return False
        else:
            filewriter.write(data)
            print("tweet %s Loaded..." % i)
            i += 1
            return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    # This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    filewriter.close()
