# unixproject
##traveltool
This consists of three main applications.
*Finding the running status of a train
*Downloading a book from the internet
*Enquiring about hotels in a city 
 
 For all of these applications, beautifulsoup4 is needed, as well as requests module. If these modules aren't present installer.sh will ask your permission and install the required modules. 
 
 
The traveltool.sh file runs the other files depending on the options given to it. 
- "bash traveltool.sh -r" runs the rail.py file, which allows you to enter the train number of the required train. Howerever "bash traveltool.sh -r update" runs updstat.py, which checks whether the status of the train checked most recently has changed or not. If it has changed, the change is updated in the file status.
- "bash traveltool.sh -h" runs hotel.py file, which works with the selenium webdriver. Note that the selenium webdriver doesn't work with Firefox 47. This particular tool has been written only for firefox. Also, after the selenium webdriver opens the browser, you need to minimize it to continue with the application. Don't close the web browser or the apllication will be aborted.
- "bash traveltool.sh" by default runs bookdownload.py.
