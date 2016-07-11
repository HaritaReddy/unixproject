#CHECKS IF THE STATUS OF PREVIOUSLY SEARCHED TRAIN HAS AT THE CURRENT TIME
import utility
import os
import sys
import re
import datetime
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

date=datetime.datetime.now()
if date.day<10:
 daystring="0"+str(date.day)
else:
 daystring=str(date.day)

if date.month<10:
 monthstring="0"+str(date.month)
else:
 monthstring=str(date.month)

yearstring=str(date.year)

total=yearstring+monthstring+daystring
f=open('status','r')
content=f.readlines()
number=content[0]


number=number[0:5]
tocall='http://runningstatus.in/' + 'status/' + number + '-on-' + total

statuspage=requests.get(tocall)
statuspage.raise_for_status()

statuspagecontent=bs4.BeautifulSoup(statuspage.text,"lxml")

infobar=statuspagecontent.select('.runningstatus-widget-content')

classtext=infobar[1].getText()
trstatus=""

for item in classtext:
 if item=="\n":
  break
 trstatus=trstatus+item

cmpstat=trstatus

trstatus=str(number)+"\n"+trstatus


stored=""
for i in range(1,len(content)):
 stored=stored+content[i]
stored=stored[0:len(stored)]


if stored==cmpstat:
 print "THERE HAS BEEN NO CHANGE IN THE STATUS OF THE TRAIN. PLEASE CHECK AFTER SOMETIME"
else:
 print trstatus

f.close()

f=open('status','w')
f.write(trstatus)
f.close()
 
