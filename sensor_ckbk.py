import RPi.GPIO as GPIO
import time

#GPIO.cleanup()

GPIO.setmode(GPIO.BCM)

a_pin = 18
b_pin = 23

def discharge():
	#print("in disch")
	GPIO.setup(a_pin, GPIO.IN)
	GPIO.setup(b_pin, GPIO.OUT)
	GPIO.output(b_pin, False)
	time.sleep(0.005)

def charge_time():
	GPIO.setup(b_pin, GPIO.IN)
	GPIO.setup(a_pin, GPIO.OUT)
	count = 0
	GPIO.output(a_pin, True)
	while not GPIO.input(b_pin):
		#print(count)
		count = count + 1
	return count

def analog_read():
	#print("in ana read")
	discharge()
	return charge_time()

try: 
	while True:
		#print("in while")
		print(analog_read())
		time.sleep(1)

except KeyboardInterrupt: 
	GPIO.cleanup()	

