import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# this is the input pin. For the 
# Vernier gate, this is pin 0 (DIO0)
a_pin = 18 

GPIO.setup(a_pin, GPIO.IN)

# define initial settings
start = time.time()
stop = time.time()
firstcross = False
secondCross = False
crosses = 0
# initial gate state with light
gateState = True 

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

