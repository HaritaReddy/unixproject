#FOR DOWNLOADING MENUS OF RESTAURANTS
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

