import requests
from bs4 import BeautifulSoup
import time
import pandas as pd



url = 'https://www.coingecko.com/'

#check amount of pages via scraping the website
def max_page(url_):
    response = requests.get(url_)

    if response.status_code == 200:

        soup = BeautifulSoup(response.content, 'html.parser')
        pagination = soup.find('nav', class_='gecko-pagination-nav')
        if pagination:
            pages = pagination.find_all(['span', 'a'], class_=['tw-text-primary-600', 'tw-cursor-pointer'])
            page_count = []

            for page in pages:
                page_t = page.text.strip()
                if page_t.isdigit():
                    page_count.append(int(page_t))
            
            max_page = max(page_count)
            
            return max_page
        else:
            return "error cannot find pagination"
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)


#input conditions

cond_1 = True

while cond_1 == True:
    print("max page on website is: 141")
    pages_ = input("how many pages would you like to scrap?: ")
    int_pages = int(pages_)
    if int_pages > 141 or int_pages < 1:
        print ("Incorrect number of pages add proper number")
    else:
         cond_1 == False


def main_scrape(url_):

    response = requests.get(url_)
    if response.status_code == 200:
        tb_data = []
        
        for i in range(1, int_pages+1):
            parameters = {'page':i}
            result = requests.get(url, params=parameters)
            print(f"scraping page: {i}")

        #table.append(pd.read_html(str(soup))[0])
        if result.status_code == 200:       
                soup = BeautifulSoup(result.content, 'html.parser')
                tb_data.append(pd.read_html(str(soup))[0]) #table is the first element
        else: 
                    print(f"Failed to retrieve data about crypto currencies from page {i}: ", result.status_code)
        
        return tb_data
        
    else:
        print("Failed to retrieve the page. Status code:", response.status_code)



if __name__ == 'scraper':
     while True:
          tb_data = main_scrape(url)
          main_tb = pd.concat(tb_data)

          # Remove the first and last columns
          main_tb.drop(main_tb.columns[[0, -1]], axis=1, inplace=True)

          print(tb_data)
          wait = 5 #change to input  so user can say how many seconds/minutes he wants
          print(f"updating after {wait} seconds")

          time.sleep(wait*60)
     