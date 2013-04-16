#!/usr/bin/python

import twitter
import sys
from ConfigParser import SafeConfigParser
from sets import Set

# Sorting function to remove all duplicate users when searching for hashtags.
# In some cases the same user may have tweeted multiple times in a row
# with the same hashtag. This will create duplicate names. So by running the 
# list of matched tweets through this function, duplicates can be removed.
def removeDuplicates(seq, idfun=None): 
   # order preserving
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result

 
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


# Query for tweets with the hashtag provided by the user

query = api.GetSearch("#" + str(sys.argv[1]), per_page=1000)

# Loop through results and print out usernames

twitterBot = api.GetUser("eurokidd")

print "Followers: " + str(twitterBot.followers_count)
print "Following: " + str(twitterBot.friends_count)
print "Now following:"
L = []
index = 0
for tweet in query:
	user = tweet.user.screen_name
	L.insert(index+1, user)
	api.CreateFriendship(user)
 
print '\n'.join(removeDuplicates(L))
