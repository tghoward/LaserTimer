import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN)

start = time.time()
stop = time.time()
gateState = False

try:
	while True:
		if (GPIO.input(4) != gateState):
			gateState = not gateState

			if (gateState == True):
				start = time.time()
			else:
				stop = time.time()

				if stop - start > 0.001:
					print "Time: ", stop - start, "s"
					print "Speed: ", 3.3/(stop - start), "cm/s"
					print " "
except KeyboardInterrupt:
	GPIO.cleanup()

