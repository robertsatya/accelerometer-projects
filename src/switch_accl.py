#!/usr/bin/python
import time
import os
i=0 
while 1: 
	time.sleep(0.1) 
	f = open ('/sys/devices/platform/lis3lv02d/position','r') 
	data = f.read() 
	ar = data.split(',') 
	results = ar[0].replace('(',''), ar[1], ar[2].replace(')','')
	print results
	string = 'wmctrl -s num' 
	if (int(ar[0].replace('(','')) >= 90): 
		i=i+1
		os.system(string.replace('num',str(i))) 
	elif (int(ar[0].replace('(','')) <= -90): 
		i=i-1
		os.system(string.replace('num',str(i)))
	f.close()
