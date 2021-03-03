#!/usr/bin/env python
import tweepy
from textblob import TextBlob
import preprocessor
import statistics
from typing import List
import preprocessor as p

from secret import consumer_key, consumer_secret

auth = tweepy.AppAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

def get_tweets(keyword: str) -> List[str]:
    all_tweets = []
    for tweet in tweepy.Cursor(api.search, q=keyword, tweet_mode='extended', lang='en').items(10):
        all_tweets.append(tweet.full_text)
    return all_tweets

def clean_tweets(all_tweets: List[str]) -> List[str]:
    tweets_clean = []
    for tweet in all_tweets:
        tweets_clean.append(p.clean(tweet))
        return tweets_clean
    return

def get_sentiment(all_tweets: List[str]) -> List[float]:
    sentiment_scores = []
    for tweet in all_tweets:
        blob = TextBlob(tweet)
        sentiment_scores.append(blob.sentiment.polarity)
    return sentiment_scores

def generate_average_sentiment_score(keyword: str) -> int:
    tweets = get_tweets(keyword)
    tweets_clean = clean_tweets(tweets)
    sentiment_scores = get_sentiment(tweets_clean)
    
    average_score = statistics.mean(sentiment_scores)

    return average_score

if __name__ == "__main__":
    print("Which one is preferred more?")
    first_keyword = input()
    print("...or...")
    second_keyword = input()

    first_score = generate_average_sentiment_score(first_keyword)
    second_score = generate_average_sentiment_score(second_keyword)

    if(first_score > second_score):
        print(f"People think {first_keyword} is better!")
    else:
        print(f"People prefer {second_keyword} is better!")