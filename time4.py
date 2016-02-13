import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

a_pin = 18

GPIO.setup(a_pin, GPIO.IN)

try: 
	while True:
		if (GPIO.input(a_pin) == False):
			print "False"
		elif (GPIO.input(a_pin) == True):
			print "True"
		else:
			continue

		time.sleep(0.002)		


except KeyboardInterrupt: 
	GPIO.cleanup()	
