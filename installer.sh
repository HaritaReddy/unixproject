#!/bin/bash
echo "The package $1 is required to run the program. Installing the required package..."
if [ $1 = "bs4" ]
then
pip install -U beautifulsoup4 --user
else
pip install -U $1 --user
fi
