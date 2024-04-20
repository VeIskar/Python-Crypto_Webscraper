import requests
from bs4 import BeautifulSoup
import time


url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody  # Find the tbody tag
trs = tbody.contents  # Find all tr tags within 

prices = {} #dict to store the prices


