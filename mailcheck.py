from __future__ import unicode_literals

#CHECKING FOE MAIL IN GMAIL
import os
import sys
import utility

try:
 import imaplib
except Exception as ImportError:
 print "This file requires imaplib module to run. Download imapclient module?(y/n)"
 entry=raw_input()
 if entry=="y":
   os.system("bash installer.sh imaplib")
   import imaplib
 else:
  exit(0)
try:
 import imapclient
except Exception as ImportError:
 print "This file requires imapclient module to run. Download imapclient module?(y/n)"
 entry=raw_input()
 if entry=="y":
   os.system("bash installer.sh imapclient")
   from imapclient import IMAPClient
 else:
  exit(0)
try:
 import pyzmail
except Exception as ImportError:
 print "This file requires pyzmail module to run. Download pyzmail module?(y/n)"
 entry=raw_input()
 if entry=="y":
  os.system("bash installer.sh pyzmail")
  import pyzmail
 else:
  exit(0)
import getpass

HOST = 'imap.gmail.com'
USERNAME = 'lingala.harita@gmail.com'
PASSWORD = 'secret'
ssl = False

server = IMAPClient(HOST, use_uid=True, ssl=ssl)
server.login(USERNAME, PASSWORD)

