import requests
from bs4 import BeautifulSoup
import requests_html  
import time
import pandas as pd



url = 'https://www.coingecko.com/'
response = requests.get(url)


dict_data = {} #dict to store data
table = []



if response.status_code == 200:
    
    
    for i in range(1,11): #first 10 pages
       parameters = {'page':i}
       result = requests.get(url,params=parameters)

       #table.append(pd.read_html(str(soup))[0])
       if result.status_code == 200:
           
            soup = BeautifulSoup(result.content, 'html.parser')
            table.append(pd.read_html(str(soup))[0])  # data frame to the list

       else: 
            print(f"Failed to retrieve page data {i}: ", result.status_code)
    
else:
    print("Failed to retrieve the page. Status code:", response.status_code)


main_tb = pd.concat(table)
