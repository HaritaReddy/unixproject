#!/bin/bash/
var=$(ls -Art | tail -n 3 | sed -n '3p') 
var2=`whoami`
if [ $1 = "home" ]
then
addr="/home/$var2"
else
addr="/home/$var2/$1"
fi

mv "$var" $addr
