import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23

GPIO.setup(a_pin, GPIO.IN)
GPIO.setup(b_pin, GPIO.IN)

start = time.time()
stop = time.time()
gateState = False
gateTwoState = False
crosses = 0

led_gpio = 4
GPIO.setup(led_gpio, GPIO.OUT)

try: 
	while True:
		if (GPIO.input(a_pin) != gateState):
			gateState = not gateState
			
			if (gateState == True):
				crosses = crosses + 1

			if (gateState == True and crosses%2 == 1):
				start = time.time()
				print "first gate triggered" 
			
		
		if (GPIO.input(b_pin) != gateTwoState):
			gateTwoState = not gateTwoState
			
			if (gateTwoState == True):
				crosses = crosses + 1
	
			if (gateTwoState == True and crosses%2 == 0):
				stop = time.time()
				print "second gate ..."
				if stop - start > 0.01:
					print "... Time: ", stop - start, "s"

		if (GPIO.input(a_pin) == True):
			GPIO.output(led_gpio, False)
		else:
			GPIO.output(led_gpio, True)	
		

except KeyboardInterrupt: 
	GPIO.cleanup()	

