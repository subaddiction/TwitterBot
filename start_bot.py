#!/usr/bin/python

import twitter
import sys
import argparse
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

# Command-line argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-hashtag", help="Unfollow users", action='store', type=str)
parser.add_argument("-add", help="Follow users", action='store_true')
parser.add_argument("-delete", help="Unfollow users", action='store_true')
args = parser.parse_args()

# Authenticate with twitter to use the Twitter API
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)

# Query for tweets with the hashtag provided by the user
query = api.GetSearch("#" + str(args.hashtag), per_page=50)

if args.add:
	print args.add
	# Create a list for all the users found using the specified hashtag.
	# Interate through the list and create friendships (Follow them)
	L = []
	index = 0
	for tweet in query:
		user = tweet.user.screen_name
		L.insert(index+1, user)
	#	api.CreateFriendship(user)

	# Remove duplicates for clarity
	print '\n'.join(removeDuplicates(L))
	print "Followers: " + str(twitterBot.followers_count)
	print "Following: " + str(twitterBot.friends_count)
	print "Now following:"

if args.delete:
	# Loop through friends and unfollow the 20 most recent followings.
	#currentFriends = api.GetFriends()
	#for f in currentFriends[:100]:
	#	print f.screen_name
	#	removeUser = api.DestroyFriendship(f.screen_name)


