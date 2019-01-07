import RPi.GPIO as GPIO
import time

class lightsAPI:
	red_pin = -1
	blue_pin = -1
	green_pin = -1
	red_pin = 0
	blue_pin = 0
	green_val = 0
	blue_val = 0
	red_val = 0

	DEFAULT_PWM_HZ = 50
	PIN_TYPE = GPIO.BOARD

	def __init__(self, red_pin, blue_pin, green_pin):
		self.red_pin = red_pin
		self.blue_pin = blue_pin
		self.green_pin = green_pin

		self.init_lights()

	def set_all_colors(self, r, g, b):
		print(r,g,b)

		self.set_green_light(self.map_rbg_pwm(g))
		self.set_red_light(self.map_rbg_pwm(r))
		self.set_blue_light(self.map_rbg_pwm(b))

	def slow_rainbow(self):
		r = 0
		g = 0
		b = 0
		FADE_SPEED = 0.05
		"""
		for r in range(0,255):
			self.set_all_colors(r,g,b)
			time.sleep(FADE_SPEED)
			r += 1

		for b in range(0,255):
                        self.set_all_colors(r,g,b)
			time.sleep(FADE_SPEED)
                        b -= 1

		for g in range(0,255):
                        self.set_all_colors(r,g,b)
			time.sleep(FADE_SPEED)
                        g += 1

		for r in range(0,255):
                        self.set_all_colors(r,g,b)
			time.sleep(FADE_SPEED)
                        r -= 1

		for b in range(0,255):
                        self.set_all_colors(r,g,b)
			time.sleep(FADE_SPEED)
                        b += 1

		for g in range(255,0):
                        self.set_all_colors(r,g,b)
			time.sleep(FADE_SPEED)
                        g -= 1
		"""
	def alternative_rainbow(self):
		r = 0
		g = 0
		b = 255
		FADE_SPEED = 0.05


		while( r < 255):
			self.set_duty_cycle(r,g,b)
			time.sleep(FADE_SPEED)
			r += 1

		while( b > 0):
                        self.set_duty_cycle(r,g,b)
                        time.sleep(FADE_SPEED)
                        b -= 1

		while( g < 255):
                       self.set_duty_cycle(r,g,b)
                       time.sleep(FADE_SPEED)
                       g += 1

	def set_green_light(self, green_val):
		self.green_val = green_val
		self.clean_up()
		self.init_lights()

	def set_blue_light(self, blue_val):
                self.blue_val = blue_val
                self.clean_up()
                self.init_lights()

	def set_red_light(self, red_val):
                self.red_val = red_val
                self.clean_up()
                self.init_lights()

	def greenify_lights(self):

		self.set_green_light(100)
		self.set_red_light(0)
		self.set_blue_light(100)

	def blueify_lights(self):
                self.set_green_light(100)
                self.set_red_light(100)
                self.set_blue_light(0)

	def redify_lights(self):
                self.set_green_light(0)
                self.set_red_light(100)
                self.set_blue_light(100)

	def map_rbg_pwm(self, rgb):
		return  (float(int(rgb) - 0) / float(255-0) ) * (100-0) + 0

	def set_duty_cycle(self, r, g, b):
		print(self.map_rbg_pwm(r),self.map_rbg_pwm(g),self.map_rbg_pwm(b))
		self.pwm_red.ChangeDutyCycle(self.map_rbg_pwm(r))
		self.pwm_blue.ChangeDutyCycle(self.map_rbg_pwm(b))
		self.pwm_green.ChangeDutyCycle(self.map_rbg_pwm(g))

	def init_lights(self):
                GPIO.setmode(self.PIN_TYPE)
                ##Set up pins as output
                GPIO.setup(self.red_pin, GPIO.OUT)
                GPIO.setup(self.blue_pin, GPIO.OUT)
                GPIO.setup(self.green_pin, GPIO.OUT)

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
#	lightsAPI = lightsAPI(7,5,3)

#	lightsAPI.alternative_rainbow()
#	lightsAPI.set_all_colors(255,165,0)
#	time.sleep(2)
#	lightsAPI.alternative_rainbow()
#	lightsAPI.clean_up()

