from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://wikipedia.org")

#   Basic web crawl
# print(html.read())

bsobject = BeautifulSoup(html.read(),"html.parser")

#   Will only include h1 elements
# print(bsobject.h1)

#   Will only include the title element
print(bsobject.title)