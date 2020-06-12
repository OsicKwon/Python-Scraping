# examples collected

import requests
from bs4 import BeautifulSoup

r = requests.get("<add your URL here>")
soup = BeautifulSoup(r.content)

for a_tag in soup.find_all('a', class_='listing-name', href=True):
    print 'href: ', a_tag['href']    [Python3]  → print( 'href: ', a_tag['href''])
