import bs4
import re
#Gives month number based on the name
def givemonth(obj):
 months={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
 return months[obj]
 
#For printing train status table
def gettable(text):
 mytable=text.select('table')
 rowlist=mytable[0].select('tr')
 headers=(rowlist[0]).select("th")
 for i in range(0,5):
  print "%25s"%(headers[i].getText()),
 print "\n"
 for i in range(1,len(rowlist)):
  rowitems=rowlist[i].select("td")
  num=len(rowitems)
  if num==7:
   num=num-2
  for j in range(0,num):
   print "%25s" %(rowitems[j].getText()),
  print "\n"

