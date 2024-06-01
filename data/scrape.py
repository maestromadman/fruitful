import requests
import re 
from bs4 import BeautifulSoup

def get_html(url):
    response = requests.get(url)
    return response.text

url_to_scrape = "https://www.traderjoes.com/home/products/pdp/fresh-mozzarella-cheese-snackers-070925"
html_document = get_html(url_to_scrape)

soup = BeautifulSoup(html_document, 'html.parser') #htmllib5
#print(soup)

for a in soup.find_all('meta', limit=10):
    print(a)

