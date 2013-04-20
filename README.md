TwitterBot
==========

A python application which searches for user specified hashtags. 
When a match is found the application will attempt to follow 
the user.

Usage
=====

	usage: start_bot.py [-h] [-hashtag HASHTAG] [-add] [-delete]

	optional arguments:
	  -h, --help        show this help message and exit
	  -hashtag HASHTAG  Unfollow users
	  -add              Follow users
	  -delete           Unfollow users

Tasks
=====

- [ ] Handle Multiple hashtags
- [ ] Check if the user is following you
- [ ] Store results in a sqlite database
- [ ] Unfollow users after 7 days
