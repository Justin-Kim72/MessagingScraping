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


#This the code for Twilio, somehow the body would where the twitter post comes from that
#relates to the message "completion of going for a run."
 
consumer_key = 'YOUR-CONSUMER-KEY'
consumer_secret = 'YOUR-CONSUMER-SECRET'
access_token = 'YOUR-ACCESS-TOKEN'
access_secret = 'YOUR-ACCESS-SECRET'
 
auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)



for tweet in tweepy.Cursor(api.user_timeline).items():
    process_or_store(tweet._json)

#This is the twitter authentification that would go through a person's profile and list all the tweets

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
#This is checking if the tweet exists in the database
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
    tags = ["#completion of run", "#run", "#finishedrun", "#Running"]
    search(random.choice(tags))
    time.sleep(60)

#This is checking through all the tags that have anything to do with running

final FirebaseDatabase database = FirebaseDatabase.getInstance();
DatabaseReference ref = database.getReference("server/saving-data/fireblog");

public static class Posts {

    public String date_of_post;
    public String username;
    public String post_content;



    public Posts(String date_of_post, String username, String post_content) {
        // ...
    }

}

DatabaseReference postsRef = ref.child("posts");

Map<String, Posts> posts = new HashMap<String, Post>();
usersRef.child("@djkhaled").setValue(new User("April 28 2017", "Available everywhere! #DJKHALED   #IMTHEONE FEAT. @justinbieber, @QuavoStuntin, @chancetherapper & @LilTunechi"));
usersRef.child("@drake").setValue(new User("April 25 2017", "Hosting first-ever NBA Awards on TNT, June 26th - tune in."));

usersRef.setValue(posts);

#This would kind of be how the firebase would work, depending on how you would do it, but let's say if we did
#it with multiple people and looking for a post that fits our description, we would add the date, the username, and the
#post content to the firebase database. 