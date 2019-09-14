import RPi.GPIO as GPIO
import time
from math import ceil
import pigpio


class lightsAPI:
	green_val = 255
	blue_val = 255
	red_val = 255

	DEFAULT_PWM_HZ = 50
	PIN_TYPE = GPIO.BCM

	def __init__(self, red_pin, blue_pin, green_pin):
		self.red_pin = red_pin
		self.blue_pin = blue_pin
		self.green_pin = green_pin
		self.pi = pigpio.pi()
		self.init_lights()

	def set_green_light(self, green_val):
		self.pi.set_PWM_dutycycle(self.green_pin, green_val)

	def set_blue_light(self, blue_val):
                self.pi.set_PWM_dutycycle(self.blue_pin, blue_val)

	def set_red_light(self, red_val):
                self.pi.set_PWM_dutycycle(self.red_pin, red_val)

	def greenify_lights(self):
		self.set_green_light(255)
		self.set_red_light(0)
		self.set_blue_light(0)

	def blueify_lights(self):
                self.set_green_light(0)
                self.set_red_light(0)
                self.set_blue_light(255)

	def redify_lights(self):
                self.set_green_light(0)
                self.set_red_light(255)
                self.set_blue_light(0)

	def yellowify_lights(self):
                self.set_green_light(255)
                self.set_red_light(255)
                self.set_blue_light(0)

	def cyanify_lights(self):
                self.set_green_light(255)
                self.set_red_light(0)
                self.set_blue_light(255)

	def magentify_lights(self):
                self.set_green_light(0)
                self.set_red_light(255)
                self.set_blue_light(255)

	def map_precent_pwm(self, precent):
		return 255 - ceil((float(int(precent) - 0) / float(100-0) ) * (255-0))

	def map_rbg_pwm(self, rgb):
                return  100 - ceil((float(int(rgb) - 0) / float(255-0) ) * (100-0))


	def init_lights(self):
#                self.clean_up()
#                GPIO.setwarnings(False) 
#                GPIO.setmode(self.PIN_TYPE)
                print("In init lights", self.red_pin, self.blue_pin, self.green_pin)
                self.pi.set_PWM_dutycycle(self.red_pin, 255)
                self.pi.set_PWM_dutycycle(self.blue_pin, 255)
                self.pi.set_PWM_dutycycle(self.green_pin, 255)
                ##Set up pins as output
#                GPIO.setup(self.red_pin, GPIO.OUT)
#                GPIO.setup(self.blue_pin, GPIO.OUT)
#                GPIO.setup(self.green_pin, GPIO.OUT)

#                self.pwm_red = GPIO.PWM(self.red_pin, self.DEFAULT_PWM_HZ)
#                self.pwm_red.start(self.red_val)
#                self.pwm_blue = GPIO.PWM(self.blue_pin, self.DEFAULT_PWM_HZ)
#                self.pwm_blue.start(self.blue_val)
#                self.pwm_green = GPIO.PWM(self.green_pin, self.DEFAULT_PWM_HZ)
#                self.pwm_green.start(self.green_val)

	def clean_up(self):
		self.pi.set_PWM_dutycycle(self.red_pin, 0)
		self.pi.set_PWM_dutycycle(self.blue_pin, 0)
		self.pi.set_PWM_dutycycle(self.green_pin, 0)

#if __name__ == "__main__":
#	print("Ready to go!")
#	lightsAPI = lightsAPI(17,22,24)
#	lightsAPI.clean_up()
#	lightsAPI.magentify_lights()
#	time.sleep(5)
#	lightsAPI.alternative_rainbow()

#	lightsAPI.set_all_colors(0,0,0)
	#lightsAPI.set_green_light(20)

#	time.sleep(5)
#	lightsAPI.alternative_rainbow()
#	lightsAPI.clean_up()

