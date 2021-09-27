import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
red = 26 #LED3
blue = 19 #LED2
green = 13 #LED1
f = 1     # frequency (Hz)
dc = 50   # duty cycle (%)
inBlue = 21
inGreen = 24
GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(inBlue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(inGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


def blink():
  pwm3= GPIO.PWM(red, f)        # create PWM object
  try:
    pwm3.start(dc)             # initiate PWM object
    while True:
      pass
  except KeyboardInterrupt:   # stop gracefully on ctrl-C
    print('\nExiting')
  pwm3.stop()
  GPIO.cleanup()

    
def fadeBlue():
  pwm2 = GPIO.PWM(blue, 100)          # create PWM object @ 100 Hz

  try:
    pwm2.start(0)                  # initiate PWM at 0% duty cycle
    while 1:
      for dc in range(101):       # loop duty cycle from 0 to 100
        pwm2.ChangeDutyCycle(dc)   # set duty cycle
        sleep(0.01)               # sleep 10 ms
      for dc in range(100, 0, -1):       # loop duty cycle from 0 to 100
        pwm2.ChangeDutyCycle(dc)   # set duty cycle
        sleep(0.01) 
  except KeyboardInterrupt:       
    print('\nExiting')
  pwm2.stop()
  GPIO.cleanup()

def fadeGreen():
  pwm1 = GPIO.PWM(green, 100)          # create PWM object @ 100 Hz

  try:
    pwm1.start(0)                  # initiate PWM at 0% duty cycle
    while 1:
      for dc in range(101):       # loop duty cycle from 0 to 100
        pwm1.ChangeDutyCycle(dc)   # set duty cycle
        sleep(0.01)               # sleep 10 ms
      for dc in range(100, 0, -1):       # loop duty cycle from 0 to 100
        pwm1.ChangeDutyCycle(dc)   # set duty cycle
        sleep(0.01) 
  except KeyboardInterrupt:       
    print('\nExiting')
  pwm1.stop()
  GPIO.cleanup()

fadeGreen()


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

