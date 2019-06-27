import requests
import csv
import time
from bs4 import BeautifulSoup

url = "https://old.reddit.com/r/buildapcsales/new/"

# mimic a browser visit
headers = {'User-Agent': 'Mozilla/5.0'}

def getItems():
	
	while True:
		page = requests.get(url, headers=headers)
		soup = BeautifulSoup(page.text, "html.parser")
		listings = soup.find_all("a")
		results = []
		categories = []
		items = []
		cats = []

		for i in listings:
			if (i.text != ''):
				if (i.text[0] == '['):
					category = i.text[i.text.find("[") + 1:i.text.find("]")]
					category = category.lower()
					if (category == "keyboard" or category == "mouse"):
						results.append(i)
						categories.append(category)
		for j in results:
			seen = False
			try:
				f = open("log.txt")
			except:
				f = open("log.txt", "a")
				f.close()
				f = open("log.txt")
			for x in f:
				if (x == j.text + "\n"):
					seen = True
			if (not seen):
				f.close()
				f = open("log.txt", "a")
				f.write(j.text + "\n")
				f.close()
				items.append(j)
				cats.append(categories[results.index(j)])
		return items, cats	