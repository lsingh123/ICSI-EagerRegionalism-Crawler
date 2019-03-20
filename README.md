#EAGER-Regionalism

My web crawlers for ICSI's Eager Regionalism project studying the balkanization of the Internet through geoblocking.

#Twitter Search

##GENERAL

This program searches Twitter for a specified number of Tweets for a specified list of queries and returns a text file of the tweets.

It also provides a function to construct a bar chart of the number of tweets by location.

##PREREQ

twitter API

install in terminal using —> pip3 install twitter

matplotlib

install in terminal using —> pip3 install matplotlib

download the TwitterSearchV2 file from the Drive folder, and make sure that the SearchTwitter.sh file and the TwitterSearchV2.py file are in the same directory

##USAGE

Run the script from the terminal:
1. Set cd to the directory that the SearchTwitter script is located in.
2. Type chmod +x SearchTwitter.sh
3. Run the script by typing ./SearchTwitter.sh
4. Follow prompts for user input.

You should see this output once execution is finished: “The program has finished executing”

#Google Search

##GENERAL

This program searches Google for various keywords and returns a text file of the HTML responses of each URL found.

##PREREQ

google API

install in terminal using —> pip3 install google

BeautifulSoup

install in terminal using —-> pip3 install bs4

html2text

install in terminal using —-> pip3 install html2text

selenium

install in terminal using —-> pip3 install selenium

You will need the ChromeDriver. It can be downloaded at this link: https://sites.google.com/a/chromium.org/chromedriver/

Once you download ChromeDriver, add its location to the system PATH. When the program runs, it will ask you to input the path where chromedriver is located.

Download the GoogleSearchV2 file from the Drive folder, and make sure that the SearchGoogle.sh file and the GoogleSearchV2.py file are in the same directory

##USAGE

Run the script from the terminal:
1. Set cd to the directory that the SearchGoogle script is located in.
2. Type chmod +x SearchGoogle.sh
3. Run the script by typing ./SearchGoogle.sh
4. Follow prompts for user input.

You should see this output once execution is finished: “The program has finished executing”
