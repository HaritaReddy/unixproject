#!/bin/bash

if [ "$1" = "-r" ]
then
if [ "$2" = "update" ]
then 
python updstat.py
else
python rail.py
fi
elif [ "$1" = "-h" ]
then
python hotel.py
else
python bookdownload.py
fi
