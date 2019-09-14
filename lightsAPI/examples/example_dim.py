import RPi.GPIO as GPIO

import time

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BOARD)

GPIO.setup(7,GPIO.OUT)

def dim():

	red_led = GPIO.PWM(7,100)

	red_led.start(0)

	pause_time = 0.010

	for i in range(0,100+1):

		red_led.ChangeDutyCycle(i)

		time.sleep(pause_time)

	for i in range(100,-1,-1):

		red_led.ChangeDutyCycle(i)

		time.sleep(pause_time)

	GPIO.cleanup()

dim()
