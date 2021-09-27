import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)

def blink():
  pBlink = 26    # GPIO pin number
  f = 1     # frequency (Hz)
  dc = 50   # duty cycle (%)
  GPIO.setup(pBlink, GPIO.OUT)
  pwm= GPIO.PWM(pBlink, f)        # create PWM object
  try:
    pwm.start(dc)             # initiate PWM object
    while True:
      pass
  except KeyboardInterrupt:   # stop gracefully on ctrl-C
    print('\nExiting')
    
  pwm.stop()
  GPIO.cleanup()
 
import RPi.GPIO as gpio
import time# Define input port numbers:
from time import sleep

# Fade

GPIO.setmode(GPIO.BCM)

p = 19
GPIO.setup(p, GPIO.OUT)
pwm = GPIO.PWM(p, 100)          # create PWM object @ 100 Hz

try:
  pwm.start(0)                  # initiate PWM at 0% duty cycle
  while 1:
    for dc in range(101):       # loop duty cycle from 0 to 100
      pwm.ChangeDutyCycle(dc)   # set duty cycle
      sleep(0.01)               # sleep 10 ms
    for dc in range(100, 0, -1):       # loop duty cycle from 0 to 100
      pwm.ChangeDutyCycle(dc)   # set duty cycle
      sleep(0.01) 
except KeyboardInterrupt:       
  print('\nExiting')

pwm.stop()
GPIO.cleanup()

# Blink

in1, in2 = 21, 24
gpio.setmode(gpio.BCM)
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN) 

def myCallback(pin):
  print("Rising edge detected on pin %d"% pin)# Execute myCallback() if port 1 goes HIGH:
gpio.add_event_detect(in1, gpio.RISING, callback=myCallback, bouncetime=200)# Infinite loop:
while True:
  print('.', end='')
  time.sleep(0.1)
gpio.cleanup()

myCallback()