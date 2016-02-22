#!/usr/bin/env python

import RPi.GPIO as GPIO
import time
import os.path

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23

GPIO.setup(a_pin, GPIO.IN)
GPIO.setup(b_pin, GPIO.IN)

#start = time.time()
#stop = time.time()
gateState = False
gateTwoState = False

if (GPIO.input(a_pin) == False):
	print "first sensor ready"
else:
	print "check first sensor alignment"

if (GPIO.input(b_pin) == False):
	print "second sensor ready"
else:
	print "check second sensor alignment"

outfile = os.path.expanduser("~/LaserTimer/carTimes.txt")

try: 
	for i in range(5):
		run = raw_input("Team and run number: ")
		print "ready for " + run
		firstIn = False 
		firstOut = False
		while True:
			if (GPIO.input(a_pin) == True ):
				if (firstIn == False):
					start = time.time()
					print "first gate triggered"
					firstIn = True
					
			if (GPIO.input(b_pin) == True ):
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

