from bs4 import BeautifulSoup
import urllib3
import requests
url = "https://parahumans.wordpress.com/2011/06/11/1-1/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html5lib")

for divtag in soup.find_all('div', {'class': 'entry-content'}):
    for ptag in divtag.find_all('p'):
        print ptag.text

##table = soup.find_all('p', {'class': "entry-content"})
##x = soup.find_all('p', class_='entry-content')
##print x
