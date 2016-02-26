import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 23 

GPIO.setup(a_pin, GPIO.IN)

start = time.time()
stop = time.time()
gateState = False
firstcross = False
secondCross = False
crosses = 0

try: 
	while True:
		if (GPIO.input(a_pin) != gateState):
			gateState = not gateState
			
			if (gateState == True):
				crosses = crosses + 1

			if (gateState == True and crosses%2 == 1):
				start = time.time()
				print "first gate triggered" 
			
			if (gateState == True and crosses%2 == 0):
				stop = time.time()
				print "second gate ..."
				if stop - start > 0.1:
					print "... Time: ", stop - start, "s"
	
		
except KeyboardInterrupt: 
	GPIO.cleanup()	

