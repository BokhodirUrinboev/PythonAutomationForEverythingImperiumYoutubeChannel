import requests
from bs4 import BeautifulSoup
url = 'https://uztelecom.uz/ru/chastnym-litsam/mobilnaya-svyaz-1/gsm/pakety/internet-pakety-3'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
table = soup.find('div', class_='tableResponsive singleMobilePackage')
headings = table.find('thead').find_all('td')
body = table.find('tbody').find_all('tr')
stringHeadings=''
for i in headings:
    stringHeadings = stringHeadings + i.text.strip('\n') + " | "
print(stringHeadings)
for i  in body:
    data = i.find_all('td')
    databody = ''
    for j in data:
        databody = databody.strip('\n') + str(j.text.strip('\n')).replace(" ","") +" | " 
    print('\n')
    print(databody)    