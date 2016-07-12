#PROGRAM TO DOWNLOAD ePUB BOOKS
import os
import sys
import utility
import re
try:
 import requests
except Exception as ImportError:
 os.system("bash installer.sh requests")
 import requests
try:
 import bs4
except Exception as ImportError:
 os.system("bash installer.sh bs4")
 import bs4
from selenium import webdriver
options=requests.get('http://www.bookrix.com/books;poetry,id:38.html')

options.raise_for_status()
#The above line checks if the retrieval of HTML page is successful or not

content=bs4.BeautifulSoup(options.text,"lxml")
#Gets the content of the html page

chunks=content.select(".chunks")

print chunks[2].getText()
print "Select the book category"
print "Type in exactly the same words"

category=raw_input()

find=chunks[2].select('a')

for i in range(0,len(find)):
 if (find[i].getText()).lower()==category.lower():
  link=(find[i])['href']
  break

goto="http://www.bookrix.com" + link

options=requests.get(goto)
options.raise_for_status()
content=bs4.BeautifulSoup(options.text,"lxml")

titlelist=content.select(".item-title")
authorlist=content.select(".item-author")

m=len(titlelist)

for i in range(0,m-1):
 print i+1," ",titlelist[i].getText()," ",authorlist[i].getText()

print "Enter option number"
num=int(raw_input())
key=num-1
bookname=titlelist[key].getText()
link="http://www.bookrix.com" + ((titlelist[key].select('a'))[0])['href']

options=requests.get(link)
options.raise_for_status()
content=bs4.BeautifulSoup(options.text,"lxml")

maincont=content.select('#bookfree')
factors=maincont[0].select('a')

link="http://www.bookrix.com" + (factors[0])['href']

options=requests.get(link)
options.raise_for_status()
content=bs4.BeautifulSoup(options.text,"lxml")

text=content.select("p")

f = open("inter", 'w')

for item in text:
  f.write(item.encode('utf-8'))
  f.write('\n')
# f.write(item.getText().encode('utf-8'))
# f.write('\n\n')

f.close()


os.system("bash refine.sh")
 
os.system("bash save.sh")

