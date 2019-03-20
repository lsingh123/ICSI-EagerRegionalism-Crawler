
import twitter
import matplotlib.pyplot as plt


#a class to serve as the twitter crawler
class TwitterSearch:
    #initializes the dictionary of locations that users tweet from
    places = {"None" : 0}
   
    def __init__():
        return

        
        
#takes keywords and number of tweets to display per keyword as parameters
#and returns a file called "TwitterSearchResults"
#with the tweets sorted by keyword
    def SearchTwitter( number=100, keywords=['geoblocking', 'not available in your country', 'website access denied', 'blocking a country'], filename="TwitterSearchResults.txt" ):
        #sets up an api object using my OAuth2 credentials
        api = twitter.Api(
            consumer_key= '3fu3c7vYiGoM3gPtcVuqWg2wZ',
            consumer_secret = '0099tU8JnIVdzQKzEe55pIQg02pSadBD7i01XeH5ULS5LEMwf9',
            access_token_key= '877999028792721408-WiyMcK7ELlU5vet2Mhoz7gGCGa6meoo',
            access_token_secret= 'PBAxBHbhPjHyr0VofZnRl4u87FtWZAbVF9BuiMaO0Vy2A'
            )
        results = open(filename, encoding = 'utf-8', mode='w+')
        #iterates through each keyword in the list of keywords to search
        for keyword in keywords:
            results.write('Results for ' + keyword + '\n\n')
            results.write('')
            #creates a list of tweet objects using the Twitter API's GetSearch method
            search = api.GetSearch(term=keyword, count=number)
            #write the information from each tweet in the search list
            for tweet in search:
                results.write(tweet.user.screen_name + ' (' + tweet.created_at + ')\n\n')
                results.write("https://twitter.com/statuses/" + tweet.id_str + '\n\n')
                results.write(tweet.text + '\n\n')
                #code to extract the location of the tweet if the user has turned geoloction on
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
        return

    
    #creates a barchart of the places dictionary
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
        return

     #user interface that prompts the user to enter the needed parameters
if __name__ == "__main__":
        print("Would you like to use the default keywords? (Y/N)")
        answer = input()
        if (answer == "Y"):
            print("How many tweets would you like to find?")
            tweets = input()
            print("What would you like to call your results file?")
            filename=input()
            TwitterSearch.SearchTwitter(number=int(tweets), filename=filename)
        else:
            print("How many keywords would you like to search?")
            x=input()
            count =0
            queries=[]
            while(count != x):
                print("Type the next keyword in")
                queries.append(input())
                count=count+1
            print("How many tweets would you like to find?")
            tweets = input()
            print("What would you like to call your results file?")
            filename=input()
            TwitterSearch.SearchTwitter(number=int(tweets), keywords = queries, filename=filename)
        print("Would you like to create a location graph?")
        answer2 = input()
        if (answer2 == "Y"):
            TwitterSearch.GraphPlaces()
            print("The program has finished executing")
            
        else:
            print("The program has finished executing")
            
    
