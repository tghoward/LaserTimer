#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os.path
import sys

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23

GPIO.setup(a_pin, GPIO.IN)
GPIO.setup(b_pin, GPIO.IN)

#start = time.time()
#stop = time.time()
gateState = True 
gateTwoState = True 

if (GPIO.input(a_pin) == True):
	print "first sensor ready"
else:
	print "check first sensor alignment"
        sys.exit(0)

if (GPIO.input(b_pin) == True):
	print "second sensor ready"
else:
	print "check second sensor alignment"
        sys.exit(0)

outfile = os.path.expanduser("~/LaserTimer/carTimes.txt")

try: 
	for i in range(10):
		run = raw_input("Team and run number: ")
		print "ready for " + run
		firstIn = False 
		firstOut = False
		while True:
			if (GPIO.input(a_pin) == False):
				if (firstIn == False):
					start = time.time()
					print "first gate triggered"
					firstIn = True
					
			if (GPIO.input(b_pin) == False):
				if (firstIn == True and firstOut == False):
					stop = time.time()
					print "second gate ..."
					firstOut = True
					t = stop - start
					print "... Time: ", t , "s"
					with open(outfile, "a") as f:
    						f.writelines("\n" + time.asctime() + "\n" + run + ": " + str(t))
					break

	
	GPIO.cleanup()

except KeyboardInterrupt: 
	GPIO.cleanup()	

