#HOTEL INFORMATION FROM HOTELSCOMBINED
import os
import urllib
import sys
import re
try:
 import requests
except Exception as ImportError:
 print "This program needs requests module. Type 'y' if you want to install it and 'n' to exit"
 char=raw_input()
 if char=="y":
  os.system("bash installer.sh requests")
 else:
  exit(0)
try:
 import bs4
except Exception as ImportError:
 print "This program needs bs4 module. Click 'y' if you want to install it and 'n' to exit"
 char=raw_input()
 if char=='y':
  os.system("bash installer.sh bs4")
 else:
  exit(0)
try:
 from selenium import webdriver
except Exception as ImportError:
 print "This program needs selenium module. Type 'y' if you want to install it and 'n' to exit"
 char=raw_input()
 if char=="y":
  os.system("bash installer.sh selenium")
 else:
  exit(0)
 from selenium import webdriver
from selenium.webdriver.common.keys import Keys

#This program uses selenium module and hence the web browser runs in the background. Firefox is required for this program to run succesfully
#Note that this doesn't work for Firefox 47 as it is not compatible with selenium.
print "Minimize the web browser after it launches. The launching of the browser depends on your internet speed...:P"
try:
 driver=webdriver.Firefox()
except selenium.common.exceptions.webdriverexception:
 print "It seems your web browser and its version it incompatible with selenium"
 exit(-1)
driver.get('http://www.hotelscombined.in/')
elem=driver.find_element_by_id('hc_f_id_noDates_1')
elem.click() #Selects the checkbox
elem1=driver.find_element_by_id('hc_f_id_where_1')
print "Enter the city name"
city=raw_input()
entry=city
elem1.send_keys(entry) #Sends user entry keys to the webpage's input box 
elem2=driver.find_element_by_class_name('hc_f_btn_v15')
elem2.click() #Navigates to the required webpage
choices=driver.find_element_by_id('hc_usr').find_elements_by_tag_name('div')

#Gives the possible locations
print "With " +city+ " you could mean the following. Please type in the serial number of your choice"
n=4
i=0
j=0
while j<n:
 print i+1,". ",choices[j].text
 i=i+1
 j=j+2
print "\n"
serial=int(raw_input("Enter the serial number>>"))
serial=serial-1
i=0
j=0
pos=0
while j<n:
 if i==serial:
  pos=j
  break
 i=i+1
 j=j+2

wee=driver.find_element_by_id('hc_usr').find_elements_by_tag_name('div')
link=wee[pos].find_element_by_tag_name('a')
link.click()

hotellist=driver.current_url


hotels=requests.get(hotellist)
hotels.raise_for_status()

hotelcontent=bs4.BeautifulSoup(hotels.text,"lxml")

mylist=hotelcontent.select('#hc_sr')
listelem=mylist[0].select('h3')
for i in range(0,len(listelem)):
 print i+1,"."," ",listelem[i].getText()
 print "\n"

print "Enter the serial number of the hotel of your choice"
useript=int(raw_input())
key=useript-1;


link=listelem[key].select('a')[0]['href']
link="http://www.hotelscombined.in"+link

#MOves to the hotel page
hotelch=requests.get(link)
hotelch.raise_for_status()
cont=bs4.BeautifulSoup(hotelch.text,"lxml")

#Prints the description of the hotel
des=cont.select('#hc_htl_desc')
addr=cont.select('.hc_htl_intro_addr')
name=cont.select('.hc_htl_intro_name')
stars=cont.select('.hc_htl_intro_rating')[0]['title']
print name[0].getText(),"\n"
print "Address: ",addr[0].getText(),"\n"
print "\n",des[0].getText()
print "\n",stars

#Checks if there are any images for the hotel
imglist=cont.select('.hc_htl_gallery_thumbs')
try:
 links=imglist[0].select('a')
except IndexError:
 print"OOPs! It seems there are no images for this hotel!"
 exit(0)

finallinks=[]
for i in range(0,len(links)):
 finallinks.append(links[i]['href'])
print "\n\n"
print "There are ",len(links)," images of the hotel. How many do you want to download? Press 0 to exit."
no1=raw_input() #Takes user input
no=int(no1)
if no==0:
 exit(0)

print "Please enter the directory name in which you want to store the directory containing the images. Choose the appropriate serial number"
print "1. Downloads,2. Home Directory,3. Desktop"
choice=int(raw_input("Enter the serial number: "))



#Downloads the specified number of images
for i in range(0,no):
 ser=str(i+1)
 filename="ttpic"+ser+".jpg"
 URL=finallinks[i];
 urllib.urlretrieve(URL, filename)
#Moves the images to the directory as specified by the user
if choice==1:
 os.system("bash create Downloads")
elif choice==2:
 os.system("bash create home")
else:
 os.system("bash create Desktop")
 
