import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 18

GPIO.setup(a_pin, GPIO.IN)

start = time.time()
stop = time.time()
gateState = False
firstcross = False
secondCross = False

try: 
	while True:
		if (GPIO.input(a_pin) == False):
			print "False"
		elif (GPIO.input(a_pin) == True):
			print "True"
		else:
			print "in gateState"
			gateState = not gateState
				
			if (gateState == True and firstcross == False):
				# dowel breaks light 1st time
				start = time.time()
				firstcross = True
				print "first cross"
			elif (gateState == True and firstcross == True):
				# dowel breaks light 2nd time
				stop = time.time()
				secondcross = True
				print "second cross"
				print "Time: ", stop - start, "s"
			elif (gateState == True and secondcross == True):
				firstcross = False
				secondcross = False
			else:
				continue
			
except KeyboardInterrupt: 
	GPIO.cleanup()	

