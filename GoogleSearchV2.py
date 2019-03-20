from google import search
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import html2text
import time
import urllib
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os



class GoogleSearch:

    
    def __init__():
        return

#returns a file of HTML responses for the query
    def Search(queries, chromedriverpath, numPages, filename="GoogleSearchResponses.txt"):
        fo = open(filename, "w+")
        chromedriver = chromedriverpath
        os.environ['webdriver.chrome.driver'] = chromedriver
        driver = webdriver.Chrome(chromedriver)
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
                driver.get(url)
                element = driver.find_element_by_xpath('/html/body')
                fo.write(url + '\n')
                fo.write(str(element.text.encode('utf-8')))
                fo.write('\n\n')


        fo.close()
        driver.close()
        return

        

         #user interface that prompts the user to enter the needed parameters
if __name__ == "__main__":
            print('What is the path where chromedriver is located? ex. /Users/lavanyasingh/Downloads/chromedriver')
            path = input()
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
            GoogleSearch.Search(queries, chromedriverpath = path, numPages = int(pages), filename=filename )
            print("The program has finished executing")
 
