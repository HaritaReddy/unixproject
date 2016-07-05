#!/bin/bash
chmod +x rail.py
chmod +x hotel.py
chmod +x installer.sh
chmod +x bookdownload.py
if [ "$1" = "-r" ]
then
python rail.py
elif [ "$1" = "-h" ]
then
python hotel.py
else
python bookdownload.py
fi
