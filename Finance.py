import requests, time, pymongo
from pymongo import MongoClient
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

cluster = MongoClient("mongodb+srv://[Redacted]@most-active.dvsp2.gcp.mongodb.net/<dbname>?retryWrites=true&w=majority")
db = cluster["finance"]
collection = db["most-active"]

#Base code, Do not Edit unless changing websites
my_url = 'https://ca.finance.yahoo.com/most-active'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers = page_soup.findAll("tr")


filename = "StockPrices.csv"


def scrape():
	db['most-active'].drop()
	f = open(filename, "w")
	headers = "Symbol, Name, Price, Change, Percent Change, Volume, Average Volume, Market Cap\n"
	f.write(headers)
	print('{:<10s}{:<35s}{:>7s}{:>15s}{:>20s}{:>15s}{:>20s}{:>15s}'.format("Symbol", "Name", "Price", "Change", "Percent Change", "Volume", "Average Volume", "Market Cap"))
	print("\n")
	for i in range(1, 25):
		contain = containers[i]
		symbol = contain.find("td", {"aria-label": "Symbol"}).getText(separator="   ")
		name = contain.find("td", {"aria-label": "Name"}).getText(separator="   ")
		price = contain.find("td", {"aria-label": "Price (Intraday)"}).getText(separator="   ")
		change = contain.find("td", {"aria-label": "Change"}).getText(separator="   ")
		percent_change = contain.find("td", {"aria-label": "% Change"}).getText(separator="   ")
		volume = contain.find("td", {"aria-label": "Volume"}).getText(separator="   ")
		avg_volume = contain.find("td", {"aria-label": "Avg Vol (3 month)"}).getText(separator="   ")
		market_cap = contain.find("td", {"aria-label": "Market Cap"}).getText(separator="   ")
		f.write(symbol + "," + name + "," + price + "," + change + "," + percent_change + ","+  volume +"," + avg_volume.replace("," , ".") +","+ market_cap+ "\n")
	f.close()
while False:
	scrape()
	time.sleep(10)
