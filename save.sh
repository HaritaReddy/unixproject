#!/bin/bash/

buffer=`ls -1t | head -1`

var=`whoami`

saveplace="/home/$var/Downloads"

mv $buffer $saveplace
