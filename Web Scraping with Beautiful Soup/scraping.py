import requests
from bs4 import BeautifulSoup
url = 'http://quotes.toscrape.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text,'lxml')
quotes = soup.find_all('span',class_='text')
authors = soup.find_all('small', class_='author')
tags = soup.find_all('div', class_='quote')
for i in range(0, len(quotes)):
    tagsShow = ''
    print("Quote: "+quotes[i].text)
    print("Author: "+authors[i].text)
    tagForQuotes = tags[i].find_all('a', class_='tag')
    for tag in tagForQuotes:
        tagsShow=tagsShow + "  " + str(tag.text)
    print("Tags: "+ tagsShow)
    print("\n\n")