import requests
from bs4 import BeautifulSoup
baseUrl = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(baseUrl)
soup = BeautifulSoup(response.text, 'lxml')
urls = []
pages = soup.find('ul', class_='pagination')
links = pages.find_all('a', class_= 'page-link')
for link in links:
	pageNum = int(link.text) if link.text.isdigit() else None 
	if pageNum != None:
		href = link.get('href')
		urls.append(href)
count = 1
for url in urls:
	newUrl= baseUrl+url
	response = requests.get(newUrl)
	soup = BeautifulSoup(response.text, 'lxml')
	items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
	for item in items:
		itemName = item.find('h4', class_='card-title').text.strip('\n')
		itemPrice = item.find('h5').text
		print('%d) Price: %s,  item: %s'%(count, itemPrice, itemName))
		count = count + 1