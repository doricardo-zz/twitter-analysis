import tweepy
import jsonpickle

consumer_key = "4YCIYo3WilWA2uicXNrpaa1d0"
consumer_secret = "n27qMQvsAGGwVA3at4YPTRpum613z3oCCcZDaGEdtJ05KKMGQj"
access_token = "1155769800590864384-eoZ6vZXgLoYP1RbmHAslMknnNUO7Ap"
access_token_secret = "YFKl8wBFpQy3rgugxGswbkduT3rwUZk9rXcq8Kraq3lRL"

# Creating the authentication object
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# Setting your access token and secret
auth.set_access_token(access_token, access_token_secret)
# Creating the API object while passing in auth information
api = tweepy.API(auth)

def get_save_tweets(filepath, api, query, max_tweets=100000, lang='pt'):

    tweetCount = 0

    #Open file and save tweets
    with open(filepath, 'w') as f:

        # Send the query
        for tweet in tweepy.Cursor(api.search,q=query,lang=lang).items(max_tweets):         

            #Convert to JSON format
            f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
            tweetCount += 1

        #Display how many tweets we have collected
        print("Downloaded {0} tweets".format(tweetCount))


query = '#AgoraFalaBolsonaro'

# Get those tweets
get_save_tweets('tweets2.json', api, query)