#!/usr/bin/python

import twitter
import sys
import argparse
from ConfigParser import SafeConfigParser
#from sets import Set

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
#parser.add_argument("-delete", help="Unfollow users", action='store_true')
args = parser.parse_args()

# Authenticate with twitter to use the Twitter API
api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token, access_token_secret=access_token_secret)

# Query for tweets with the hashtag provided by the user
query = api.GetSearch("#" + str(args.hashtag), count=100)
# NOTE: one can follow 1000 accounts per day, limiting to 100 results grants 10 searches+autofollow per day

if args.add:
	# print args.add
	# Create a list for all the users found using the specified hashtag.
	# Interate through the list and create friendships (Follow them)
	L = []
	index = 0
	for tweet in query:
		user = tweet.user.screen_name
		userid = tweet.user.id
		
		L.insert(index+1, user)
		#L.insert(index+1, userid)
		#print userid, 'FOLLOWED', '(', user, ')'
	
	ToFollow = removeDuplicates(L)
	
	for user in ToFollow:
		
		#UNCOMMENT THE NEXT LINE TO ACTUALLY FOLLOW RETRIEVED USERS
		api.CreateFriendship(screen_name=user)
		#api.CreateFriendship(user_id=user)
		print user, 'FOLLOWED'
		
	
	
	#print 'FOLLOWED ACCOUNTS:'
	# Remove duplicates for clarity
	#print '\n'.join(removeDuplicates(L))
	
