# Tweepy
# Copyright 2009-2010 Joshua Roesslein
# See LICENSE for details.

"""
Tweepy Twitter API library
"""
__version__ = '2.2'
__author__ = 'Joshua Roesslein'
__license__ = 'MIT'

from tweepy.api import API

# Global, unauthenticated instance of API
api = API()

def debug(enable=True, level=1):

    import http.client
    http.client.HTTPConnection.debuglevel = level