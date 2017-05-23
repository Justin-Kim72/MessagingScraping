import tweepy
from tweepy import OAuthHandler
import os 
from twilio.rest import Client

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]

client = Client(account_sid, auth_token)

client.messages.create(
    to = "+19786186820"
    from_ = "+14352141522"
    body = "")

 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)



for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

fb_url = https://{MessagingScraping}.firebaseio.com/tweets.json

def check_tweet(tweet):
    try:
        r = requests.get(fb_url)
        r = r.json()
        for i in r:
            if tweet.id == r[i]["id"]:
                return False
    finally:
        return True
def search(tag):
    try:
        c = tweepy.Cursor(api.search, q=tag)
        print("Searching "+tag)
        i = 0 
        for tweet in c.items():
            if i < 1 and tweet.retweet_count > 20:
                if check_tweet(tweet):
                    api.retweet(tweet.id)
                    db_tweet = {"id": tweet.id}
                    requests.post(fb_url, json.dumps(db_tweet))
                    i += 1
                    break

while True:
    tags = ["#danceparty", "#ilovehats", "#firebase", "#tweepy"]
    search(random.choice(tags))
    time.sleep(60)