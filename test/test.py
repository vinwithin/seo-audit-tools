import requests
from bs4 import BeautifulSoup  # use BeautifulSoup library to scrape the websites

r = requests.get('https://siakad.um.ac.id/')
soup = BeautifulSoup(r.content, 'html.parser')
tags = soup.find('body').findChildren()

print(tags)