#GIVES THE LIVE RUNNING STATUS OF A TRAIN
import utility
import os
import sys
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

print "LIVE RUNNING STATUS OF TRAIN"
print "Enter the 5 digit train number"
number=raw_input()
if len(number)!=5:
 print "You are supposed to enter 5 digit number only!\nProgram aborted!"
 exit(3)
options=requests.get('http://runningstatus.in/')

options.raise_for_status()
#The above line checks if the retrieval of HTML page is successful or not

optobj=bs4.BeautifulSoup(options.text,"lxml")
#Gets the content of the html page

optlist=optobj.select('option')
print "Choose any of the following dates"

for i in range(0,5):
 print i+1,optlist[i].getText()

print "Enter the option number"
choice=int(raw_input())

key=choice-1
#Getting month number
month=utility.givemonth((optlist[key].getText())[8:11])
#Getting the day
day=(optlist[key].getText())[0:2]
#Getting the year
inter=optlist[key].getText()
year=re.findall('[^ ]*\s[^ ]*\s[^ ]*\s([0-9]*)\s',inter)[0]

tocall='http://runningstatus.in/' + 'status/' + number + '-on-' + year + month + day

statuspage=requests.get(tocall)
statuspage.raise_for_status()

statuspagecontent=bs4.BeautifulSoup(statuspage.text,"lxml")

infobar=statuspagecontent.select('.runningstatus-widget-content')

if infobar==[]:
 print "Invalid Train number"
 exit(3)


classtext=infobar[1].getText()
status=""

for item in classtext:
 if item=="\n":
  break
 status=status+item

print status

#Printing the entire station table
print "Do you want entire table of stations with arrival and departure times? Type 'e' for the entire table, and 'n' to exit"

mychoice=raw_input()


if mychoice=="n":
 exit(0)
else:
 utility.gettable(statuspagecontent)

 




