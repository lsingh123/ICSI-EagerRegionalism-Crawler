from google import search
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import html2text
import time
import urllib



class GoogleSearch:
    def __init__():
        return

#returns a file of HTML responses for the query
    def Search(queries, numPages, filename="GoogleSearchResponses.txt"):
        fo = open(filename, "w+")
        #iterates through each query in the queries list passed as a parameter
        for query in queries:
            fo.write(query + '\n\n')
            #pauses for 2 minutes to avoid HTTP Error 429
            time.sleep(120)
            #create a list of urls from the first numPages pages of google
            #using the query
            urlList= search(query,  stop = numPages)
            #write the html text of each url to the file
            for url in urlList:
                try:
                    req = Request(url, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
                    response = urlopen(req).read()
                    fo.write(url + "\n")
                    soup = BeautifulSoup(response, "lxml")
                    #convert raw html to more readable text
                    text = html2text.html2text(soup.get_text().replace('\n', '\n'))
                    fo.write(str(text.encode('utf-8')))
                    fo.write('\n\n\n')
                except URLError as e:
                    if hasattr(e, 'reason'):
                        print('We failed to reach a server.')
                        print('Reason: ', e.reason)
                    elif hasattr(e, 'code'):
                        print('The server couldn\'t fulfill the request.')
                        print('Error code: ', e.code)
        fo.close()
        return

        

         #user interface that prompts the user to enter the needed parameters
if __name__ == "__main__":

            print("How many keywords would you like to search?")
            x=input()
            count =0
            queries=[]
            while(count < int(x)):
                print("Type the next keyword in")
                queries.append(input())
                count=count+1
            print("How many pages of Google would you like to search?")
            pages = input()
            print("What would you like to call your results file?")
            filename=input()
            GoogleSearch.Search(queries, numPages = int(pages), filename=filename)
            print("The program has finished executing")
 
