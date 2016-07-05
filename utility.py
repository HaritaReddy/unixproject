import bs4
import re
def givemonth(obj):
 months={"Jan":"01","Feb":"02","Mar":"03","Apr":"04","May":"05","Jun":"06","Jul":"07","Aug":"08","Sep":"09","Oct":"10","Nov":"11","Dec":"12"}
 return months[obj]

def gettable(text):
 mytable=text.select('table')
 rowlist=mytable[0].select('tr')
 headers=(rowlist[0]).select("th")
# print "\n\n"
# for i in range(0,num):
#  print headers[i].getText(),"\t",
# print "\n" 
# for i in range(1,len(rowlist)):
#  rowitems=rowlist[i].select("td")
#  for j in range(0,len(rowitems)):
#  print rowitems[j].getText(),"\t",
#  print "\n"
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

