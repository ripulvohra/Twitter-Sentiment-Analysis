#importing various modules
import requests
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

#make ur app on twitter and get ur ckey,csecret,accesskey,accesstoken.
#enter consumer key, consumer secret, access token, access secret.
ckey="EKrGrMl9SbG0Qa3n1kvHxDwcp"
csecret="FtQdtFA8exg2yw4ZnwqOu0iRF2ThAFXLCbs0pDIrSGmL9XnV80"
atoken="851461746212487173-YBoswsGwa43pYWNJYG1h70zrEw6mZa0"
asecret="7zWOG2clH5muUebUfJM3dpCLzaEy8pKIoLRhEeYYDXBbu"

#to interact with sentiment analysis api
url = 'http://sentiment.vivekn.com/api/text/'

class listener(StreamListener):

    def on_data(self, data):
            try:
                all_data = json.loads(data)
                tweet = all_data["text"]
                r=requests.post(url,{'txt':tweet})
                js=json.loads(r.text[:])
                print(tweet,js['result']['sentiment'], js['result']['confidence'])

                if js['result']['confidence'] >= 80:
                        output = open("twitter-out.txt","a")
                        output.write(sentiment_value)
                        output.write('\n')
                        output.close()

                return True

            except:
               return True

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
#enter the word in track field
twitterStream.filter(track=["happy"])
