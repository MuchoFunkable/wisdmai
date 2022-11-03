import tweepy
import configparser
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyser = SentimentIntensityAnalyzer()

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# user tweets
# user = 'veritasium'
# limit=300

# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
keywords = '$TSLA'
limit = 250

tweets = tweepy.Cursor(api.search_tweets, q=keywords,
                       count=100, tweet_mode='extended').items(limit)

# tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')

# create DataFrame
columns = ['Time', 'User', 'Tweet', "Analysis"]
data = []

for tweet in tweets:
    # if tweet.user.verified == True:
    data.append([tweet.created_at, tweet.user.screen_name,
                tweet.full_text, analyser.polarity_scores(tweet.full_text)])

df = pd.DataFrame(data, columns=columns)

df.to_csv('tweets.csv')
