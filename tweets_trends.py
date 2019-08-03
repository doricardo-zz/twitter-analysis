# -*- coding: utf-8 -*-
import sys
import tweepy
import json
import jsonpickle
from datetime import datetime
import time

#Autenticações
consumer_key = "4YCIYo3WilWA2uicXNrpaa1d0"
consumer_secret = "n27qMQvsAGGwVA3at4YPTRpum613z3oCCcZDaGEdtJ05KKMGQj"
access_token = "1155769800590864384-eoZ6vZXgLoYP1RbmHAslMknnNUO7Ap"
access_token_secret = "YFKl8wBFpQy3rgugxGswbkduT3rwUZk9rXcq8Kraq3lRL"

#Open file and save tweets
trendsCount = 0

while True:

	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	# O Yahoo! Where On Earth ID para o Brasil é 23424768.
	# Veja mais em https://dev.twitter.com/docs/api/1.1/get/trends/place e http://developer.yahoo.com/geo/geoplanet/
	#BRAZIL_WOE_ID = 23424768

	country = {"23424747":"argentina",
	"23424768":"brasil",
	"23424782":"chile",
	"23424787":"colombia",
	"23424801":"equador",
	"23424919":"peru",
	"23424982":"venezuela",
	"1":"mundo"}

	for country_id, country_name in country.items():

		#try:
			trends = api.trends_place(country_id)
			trends_json = json.loads(json.dumps(trends, indent=1))

			filepath = 'tweets/trends_' + datetime.now().strftime('%Y%m%d_%H%M%S') + '_' + country_name + '.json'
			with open(filepath, 'w') as f:

				for trend in trends_json:

					f.write(jsonpickle.encode(trend, unpicklable=False) + '\n')

		#except:
		 #   print("Erro pais {0} {1}".format(country_name,errors['message']))
	
	print("Downloaded trends {0} minuto(s)...".format(trendsCount))
	trendsCount += 15

	time.sleep(900)