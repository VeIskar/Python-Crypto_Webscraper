import requests
from bs4 import BeautifulSoup
#import requests_html  
import time
import pandas as pd



url = 'https://www.coingecko.com/'
response = requests.get(url)

#check amount of pages via scraping the website
def max_page(url_):
    response = requests.get(url)

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


print(f"max page on website is: {max_page(url)}")
pages_ = input("how many pages would you like to scrap?: ")
int_pages = int(pages_)
if int_pages>max_page(url):
    print ("Too many pages")



if response.status_code == 200:
    
    tb_data = []
    
    for i in range(1,int_pages):
       parameters = {'page':i}
       result = requests.get(url, params=parameters) #.text not necessary if we later get .content
       
       print(f"scraping page: {i}")

       #table.append(pd.read_html(str(soup))[0])
       if result.status_code == 200:        
            soup = BeautifulSoup(result.content, 'html.parser')

            tb_data.append(pd.read_html(str(soup))[0]) #table is the first element

       else: 
            print(f"Failed to retrieve data about crypto currencies from page {i}: ", result.status_code)
    
else:
    print("Failed to retrieve the page. Status code:", response.status_code)


#merge the tables into one
main_tb = pd.concat(tb_data)

# Remove the first and last columns
main_tb.drop(main_tb.columns[[0, -1]], axis=1, inplace=True)

print(tb_data)
