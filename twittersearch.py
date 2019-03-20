import twitter
import geojson
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim

#a class to serve as the twitter crawler
class TwitterSearch:

    places = {"None" : 0}
   
    def __init__():
        return
        
#takes keywords and number of tweets to display per keyword as parameters
#and returns a file called "TwitterSearchResults"
#with the tweets sorted by keyword
    def SearchTwitter( number, keywords=['geoblocking', 'not available in your country', 'blocking a country'], filename="TwitterSearchResults.txt" ):
        api = twitter.Api(
            consumer_key= '3fu3c7vYiGoM3gPtcVuqWg2wZ',
            consumer_secret = '0099tU8JnIVdzQKzEe55pIQg02pSadBD7i01XeH5ULS5LEMwf9',
            access_token_key= '877999028792721408-WiyMcK7ELlU5vet2Mhoz7gGCGa6meoo',
            access_token_secret= 'PBAxBHbhPjHyr0VofZnRl4u87FtWZAbVF9BuiMaO0Vy2A'
            )
        results = open(filename, encoding = 'utf-8', mode='w+')
        for keyword in keywords:
            results.write('Results for ' + keyword + '\n\n')
            results.write('')
            search = api.GetSearch(term=keyword, count=number)
            for tweet in search:
                results.write(tweet.user.screen_name + ' (' + tweet.created_at + ')\n\n')
                results.write(tweet.text + '\n\n')
                if (str(tweet.place) != "None"):
                    country = str(tweet.place) [str(tweet.place).find('country_code')+16:str(tweet.place).find('country_code')+18]
                    results.write("country = " + country + '\n\n')
                    if country in TwitterSearch.places:
                        TwitterSearch.places[country] = TwitterSearch.places[country] + 1
                    else:
                        TwitterSearch.places[country] = 1
                else:
                    TwitterSearch.places["None"] = TwitterSearch.places["None"] + 1
            results.write('End of results for ' + keyword)
            results.write('\n')
        results.close()
        for key in TwitterSearch.places:
            print(key + " ")
            print(str(TwitterSearch.places[key]) + ' \n\n')
        return

    def GraphPlaces():
        number = 0
        left = [0]
        height = [0]
        tick_label = [None]
        number=0
        for key in TwitterSearch.places:
            left.append(number+1)
            tick_label.append(key)
            height.append(TwitterSearch.places[key])
            number=number+1
        del left[0]
        del height[0]
        del tick_label[0]
        
        
        plt.bar(left, height, tick_label=tick_label, width=0.8, color=['red', 'blue'])
        plt.ylabel('Number of Results')
        plt.title('TwitterSearchResults by Country')
        plt.show()
            

            

#a method with the addition of a location parameter
#location: string ex. "175 5th Avenue NYC"
    def SearchTwitterlocation( address, radius, number, filename = "TwitterSearchResults.txt", keywords=['geoblocking', 'not available in your country', 'blocking a country']):
        api = twitter.Api(
            consumer_key= '3fu3c7vYiGoM3gPtcVuqWg2wZ',
            consumer_secret = '0099tU8JnIVdzQKzEe55pIQg02pSadBD7i01XeH5ULS5LEMwf9',
            access_token_key= '877999028792721408-WiyMcK7ELlU5vet2Mhoz7gGCGa6meoo',
            access_token_secret= 'PBAxBHbhPjHyr0VofZnRl4u87FtWZAbVF9BuiMaO0Vy2A'
            )
        results = open(filename, encoding = 'utf-8', mode='w+')
        for keyword in keywords:
            results.write('Results for ' + keyword + '\n\n')
            results.write('')
            search = api.GetSearch(term=keyword, lang='en', count=number, geocode=TwitterSearch.getGeocode(address, radius))
            for tweet in search:
                results.write(tweet.user.screen_name + ' (' + tweet.created_at + ')\n\n')
                results.write(tweet.text + '\n\n')
            results.write('End of results for ' + keyword)
            results.write('\n')
        results.close()
        return



    
    #address: string ex. "175 5th Avenue NYC"
    #radius: string that represents radium in mi or in km ex. "1mi" or "1km"
    def getGeocode(address, radius):
        geolocator = Nominatim()
        location = geolocator.geocode(address)
        geocode = str(location.latitude) + ',' + str(location.longitude) + ',' + radius
        return geocode
    
    
