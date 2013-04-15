#!/usr/bin/python

import twitter
from ConfigParser import SafeConfigParser
from sets import Set
 
# Tell the parser which ini file to read
parser = SafeConfigParser()
parser.read('api-keys.ini')

# Read in the OAuth2 keys, secrets, and tokens for authentications
consumer_key        = parser.get('API_KEYS', 'consumer_key')
consumer_secret     = parser.get('API_KEYS', 'consumer_secret')
access_token        = parser.get('API_KEYS', 'access_token')
access_token_secret = parser.get('API_KEYS', 'access_token_secret')

# Authenticate with twitter to use the Twitter API
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)

# Query for tweets with the hashtag rogue
query = api.GetSearch("#rogue")

# Loop through results and print out usernames
for tweet in query:
	print tweet.user.screen_name