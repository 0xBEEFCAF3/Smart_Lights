import RPi.GPIO as GPIO
import time

class lightsAPI:
	red_pin = -1
	blue_pin = -1
	green_pin = -1
	red_pin = 0
	blue_pin = 0
	green_val = 100
	blue_val = 0
	red_val = 0

	DEFAULT_PWM_HZ = 150

	def __init__(self, red_pin, blue_pin, green_pin):
		self.red_pin = red_pin
		self.blue_pin = blue_pin
		self.green_pin = green_pin
		GPIO.setmode(GPIO.BOARD)
		##Set up pins as output
		GPIO.setup(red_pin, GPIO.OUT)
		GPIO.setup(blue_pin, GPIO.OUT)
		GPIO.setup(green_pin, GPIO.OUT)
		self.init_lights()

	def set_green_light(green_val):
		self.green_val = green_val
		self.clean_up()
		self.init_lights()
	
	def set_blue_light(blue_val):
                self.blue_val = blue_val
                self.clean_up()
                self.init_lights()

	def set_red_light(red_val):
                self.red_val = red_val
                self.clean_up()
                self.init_lights()

	def init_lights(self):
		self.pwm_red = GPIO.PWM(self.red_pin, self.DEFAULT_PWM_HZ)
                self.pwm_red.start(self.red_val)
                self.pwm_blue = GPIO.PWM(self.blue_pin, self.DEFAULT_PWM_HZ)
                self.pwm_blue.start(self.blue_val)
                self.pwm_green = GPIO.PWM(self.green_pin, self.DEFAULT_PWM_HZ)
                self.pwm_green.start(self.green_val)


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
	
