import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 18

GPIO.setup(a_pin, GPIO.IN)

start = time.time()
stop = time.time()
gateState = False

try: 
	while True:
		if (GPIO.input(a_pin) != gateState):
			gateState = not gateState
				
			if (gateState == True):
				start = time.time()
			else:
				stop = time.time()
			
				if stop - start > 0.001:
					print "Time: ", stop - start, "s"

			
except KeyboardInterrupt: 
	GPIO.cleanup()	

