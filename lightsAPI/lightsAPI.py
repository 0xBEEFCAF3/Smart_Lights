import RPi.GPIO as GPIO
import time

class lightsAPI:
	red_pin = -1
	blue_pin = -1
	green_pin = -1


	def __init__(self, red_pin, blue_pin, green_pin):
		self.red_pin = red_pin
		self.blue_pin = blue_pin
		self.green_pin = green_pin
		GPIO.setmode(GPIO.BOARD)
		##Set up pins as output
		GPIO.setup(red_pin, GPIO.OUT)
		GPIO.setup(blue_pin, GPIO.OUT)
		GPIO.setup(green_pin, GPIO.OUT)
		##Initialize pwm object with 50 Hz and 0% duty cycle
		self.pwm_red = GPIO.PWM(red_pin, 100)
                self.pwm_red.start(0)
		self.pwm_blue = GPIO.PWM(blue_pin, 100)
                self.pwm_blue.start(0)
		self.pwm_green = GPIO.PWM(green_pin, 100)
		self.pwm_green.start(0)
		
	def clean_up(self):
		GPIO.cleanup()
		self.pwm_blue.stop()
		self.pwm_green.stop()
		self.pwm_red.stop()



if __name__ == "__main__":
	print("Ready to go!")
	lightsAPI = lightsAPI(7,5,3)
	time.sleep(5)
	lightsAPI.clean_up()
	
