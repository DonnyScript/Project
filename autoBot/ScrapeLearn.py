import requests
from bs4 import BeautifulSoup
   
r = requests.get('https://reddit.com')

soup = BeautifulSoup(r.content, 'html.parser')

print(soup.title)

print(soup.title.name)

print(soup.title.parent.name)
