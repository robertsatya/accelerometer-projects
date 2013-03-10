#!/bin/bash

COUNTER=0

while [ $COUNTER -le 100 ]; do
	sleep 0.5
	POS=`cat /sys/devices/platform/lis3lv02d/position | awk -F "(" '{print$2}' | awk -F , '{print$1}'`
	echo $POS
		if [ $POS -ge 12 ]; then
			wmctrl -o 1024,0
		elif [ $POS -le -12 ]; then
			wmctrl -o 0,0
		fi
	COUNTER=$(( $COUNTER + 1 ))
done
