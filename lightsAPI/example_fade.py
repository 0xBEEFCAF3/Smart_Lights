
import time
import RPi.GPIO as GPIO

# Pin definitions
led_pin =  3
other_pin = 7

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BOARD)

# Set LED pin as output
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(other_pin, GPIO.OUT)
# Initialize pwm object with 50 Hz and 0% duty cycle
pwm = GPIO.PWM(led_pin, 100)
pwm.start(0)

pwm2 = GPIO.PWM(other_pin, 50)
pwm2.start(0)

# Set PWM duty cycle to 50%, wait, then to 90%
pwm.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50)
time.sleep(2)
pwm.ChangeDutyCycle(90)
pwm2.ChangeDutyCycle(90)
time.sleep(2)

# Stop, cleanup, and exit
pwm.stop()
pwm2.stop()
GPIO.cleanup()

