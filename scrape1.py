from bs4 import BeautifulSoup
import urllib3
import requests

# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib3
import requests
import re


url = "https://parahumans.wordpress.com/2011/06/11/1-1/"
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html, "html5lib")
##soup1 = soup.find("title").text


##print soup1[:-7]
##t1 = soup.find('title')
##print t1.text
##title = "Gestation 1.1 | Worm"
##title = title[:-7]
##print title
##p1 = "Hello"
##p2 = "Goodbye"
##p3 = "Forever"

##x = """<html><head></head>
##<body>
##<p style="text-align:right;">
##<a href="https://parahumans.wordpress.com/2011/06/14/gestation-1-2/" title="Next Chapter">Next Chapter</a>
##</p>
##</body></html>"""


##message = """<html></html>"""
##f.write(message)
##f.write(str(x))
##f.close()

f = open('helloworld3.html','w')

for divtag in soup.find_all('div', {'class': 'entry-content'}):
    for ptag in divtag.find_all('p'):
        for atag in ptag.find_all('a'):
            atag.replaceWith("")
        f.write(str(ptag))
f.close()

print "Finished"

##table = soup.find_all('p', {'class': "entry-content"})
##x = soup.find_all('p', class_='entry-content')
##print x

##strx = "Hello World"
##print strx.replace("Hello", "Goodbye")


##url = "https://parahumans.wordpress.com/2011/06/11/1-1/"
##response = requests.get(url)
##html = response.content
##soup = BeautifulSoup(html, "html5lib")

##for divtag in soup.find_all('div', {'class': 'entry-content'}):
##    for ptag in divtag.find_all('p'):
##        print ptag.text

##table = soup.find_all('p', {'class': "entry-content"})
##x = soup.find_all('p', class_='entry-content')
##print x
