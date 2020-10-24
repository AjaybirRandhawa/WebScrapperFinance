import requests
import re
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs

#Load the webpage Content
r = requests.get("https://keithgalli.github.io/web-scraping/example.html")
soup = bs(r.content)

#Find and Find All
first_header = soup.find("h2")#Finds the first element only not all of them
print(first_header)

headers = soup.find_all("h2") #creates a list of all h2 even if only 1 element sitll in a list
print(headers)

all_headers = soup.find_all(["h1", "h2"]) #We can also pass in a list of elements it should find
print(all_headers)

paragraphs = soup.find_all("p", attrs= {"id": "paragraph-id"}) #You can pass in other attributes such as id or name of the html file
print(paragraphs)

#You can also nest find and find all calls
body = soup.find("body")
div = body.find("div") #Now it'll only look inside the body for the divs
header = div.find("h1") #Now it'll look inside div for header
print(header)

#We can search specific strings in our find/find all calls
paragraphs = soup.find_all("p", string=re.compile("Some")) #It will use regex and find all occurances of Some inside paragraph tags
print(paragraphs)

headers = soup.find_all("h2", string=re.compile("(H|h)eader")) #Learn Regex...
print(headers)


#CSS Selectors For full possibilities look at CSS Selector Examples
paragraphs = soup.select("p")
print(paragraphs)