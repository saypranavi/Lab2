import RPi.GPIO as GPIO 
import time # Define input port numbers:
from time import sleep

GPIO.setmode(GPIO.BCM)

inBlue = 21
inGreen = 24

GPIO.setup(inBlue, GPIO.IN)

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
    
def fadeBlue():
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
# in1, in2 = 21, 24
# GPIO.setmode(GPIO.BCM)
GPIO.setup(inBlue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
# GPIO.setup(in2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) 

# def myCallback(pin):
#     print("Rising edge detected on pin %d"% pin)
GPIO.add_event_detect(inBlue, GPIO.RISING, callback=fadeBlue, bouncetime=200)
# while True:
#     print('.', end='')
#     time.sleep(0.1)
#   GPIO.cleanup()

#   myCallback()

