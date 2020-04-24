import requests

from bs4 import BeautifulSoup
page = requests.get("https://en.wikipedia.org/wiki/Lists_of_films")
soup = BeautifulSoup(page.content,'html.parser')


print(soup.title)
#l=soup.findAll(id='By_country_of_origin')
#print(l)
line_count = 1
#print(soup.findAll('a'))
for list in soup.findAll('a'):
    if line_count >= 265 and line_count<=389:
       link=list['href']
       print(link.rsplit('/',1)[1])
    line_count += 1


#