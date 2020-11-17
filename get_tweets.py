import tweepy
import time
import pandas as pd
pd.set_option('display.max_colwidth', 1000)

# api key
api_key = "4vEUQjvdrzVy9Kmzep1Y4l9zR"
# api secret key
api_secret_key = "VMvrUbScT96NYOtmC0mmDWmeQapjNv1g8CUPfchrL9Zi0x8d7f"
# access token
access_token = "1000392397308575744-wQYSYPfFVSYtXhvxdTmoUOvdtBD6R8"
# access token secret
access_token_secret = "toG3h9ncJGFAFdeqrtc6sm3KJhS13q031pj56XAttJDW4"

authentication = tweepy.OAuthHandler(api_key, api_secret_key)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication, wait_on_rate_limit=True)

def get_related_tweets(text_query):
    pd.set_option('display.max_colwidth', -1)
    # list to store tweets
    tweets_list = []
    # no of tweets
    count = 20
    try:
        # Pulling individual tweets from query
        for tweet in api.search(q=text_query, count=count):
            #print(tweet.text)
            # Adding to list that contains all tweets
            tweets_list.append({'created_at': tweet.created_at,
                                'tweet_id': tweet.id,
                                'tweet_text': tweet.text})
        return pd.DataFrame.from_dict(tweets_list)

    except BaseException as e:
        print('failed on_status,', str(e))
        time.sleep(3)


# data= get_related_tweets("donald trump")
# print(data.info())