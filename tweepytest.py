from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

ckey="3fu3c7vYiGoM3gPtcVuqWg2wZ"
csecret="0099tU8JnIVdzQKzEe55pIQg02pSadBD7i01XeH5ULS5LEMwf9"
atoken="877999028792721408-WiyMcK7ELlU5vet2Mhoz7gGCGa6meoo"
asecret="PBAxBHbhPjHyr0VofZnRl4u87FtWZAbVF9BuiMaO0Vy2A"

class listener(StreamListener):
    def on_data(self, data):
        print(data)
        return(True)
    def on_error(self, status):
        print (status)

auth = OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=["car"])
