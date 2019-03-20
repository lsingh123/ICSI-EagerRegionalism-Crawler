from TwitterSearch import *
def GeoBlocked():
   # try:
        tso = TwitterSearchOrder()
        tso.set_keywords(['geoblocking', 'geoblocked'])
        tso.set_language('en')
        tso.set_include_entities(False)
        tso.verify = False

        ts = TwitterSearch(
            consumer_key = 'aaabbb',
            consumer_secret = 'cccddd',
            access_token = '111222',
            access_token_secret = '333444'
        )
        for tweet in ts.search_tweets_iterable(tso):
            print ('@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
    #except TwitterSearchException as e:
        #print(e)
        return
