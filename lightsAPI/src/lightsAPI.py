import RPi.GPIO as GPIO
import time
from math import ceil
import pigpio
import time
from threading import Thread



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
                self.return_to_main = True

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
                self.rainbow_thread.join();

                self.set_green_light(0)
                self.set_red_light(255)
                self.set_blue_light(255)
        
        def updateColor(self, color, step):
            color += step
        
            if color > 255:
                return 255
            if color < 0:
                return 0
                
            return color

        def rainbow_lights(self, steps):
                self.STEPS = steps
                r = 255
                g = 0
                b = 0
                while True:
                    if(self.return_to_main): continue

                    if r == 255 and b == 0 and g < 255:
                            g = self.updateColor(g, self.STEPS)
                            self.set_green_light(g)
                    
                    elif g == 255 and b == 0 and r > 0:
                            r = self.updateColor(r, -self.STEPS)
                            self.set_red_light(r)
                    
                    elif r == 0 and g == 255 and b < 255:
                            b = self.updateColor(b, self.STEPS)
                            self.set_blue_light(b)
                    
                    elif r == 0 and b == 255 and g > 0:
                            g = self.updateColor(g, -self.STEPS)
                            self.set_green_light(g)
                    
                    elif g == 0 and b == 255 and r < 255:
                            r = self.updateColor(r, self.STEPS)
                            self.set_red_light(r)
                    
                    elif r == 255 and g == 0 and b > 0:
                            b = self.updateColor(b, -self.STEPS)
                            self.set_blue_light(b)

                
        
        def map_precent_pwm(self, precent):
                return 255 - ceil((float(int(precent) - 0) / float(100-0) ) * (255-0))

        def map_rbg_pwm(self, rgb):
                return  100 - ceil((float(int(rgb) - 0) / float(255-0) ) * (100-0))


        def init_lights(self):
                print("In init lights", self.red_pin, self.blue_pin, self.green_pin)
                self.pi.set_PWM_dutycycle(self.red_pin, 255)
                self.pi.set_PWM_dutycycle(self.blue_pin, 255)
                self.pi.set_PWM_dutycycle(self.green_pin, 255)

        def clean_up(self):
                self.pi.set_PWM_dutycycle(self.red_pin, 0)
                self.pi.set_PWM_dutycycle(self.blue_pin, 0)
                self.pi.set_PWM_dutycycle(self.green_pin, 0)

#obj = lightsAPI(17, 22, 24)
#obj.rainbow_lights(0.05)

#time.sleep(5000)

