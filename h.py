import RPi.GPIO as GPIO
from time import sleep # import time.sleep()

GPIO.setmode(GPIO.BCM) # use BCM port numbering
red = 26 # pin number
blue = 19
green =13
b1 =21
b2 =24
f = 1 #hertz
dc = 100
Dict = {b1: green, b2: green}


GPIO.setup(red, GPIO.OUT) # assign the pin as output
GPIO.setup(red, GPIO.OUT) # assign the pin as output
GPIO.setup(green, GPIO.OUT) # assign the pin as output
GPIO.setup(b1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(b2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#pred = GPIO.PWM(red, f)
#pgreen = GPIO.PWM(green, f)


try:
  def myCallback(pin):
    print("Rising edge detected on pin %d" % pin)
    if GPIO.input(b1) == GPIO.HIGH:
      pred = GPIO.PWM(blue, f)
      pred.start(0)
      for dc in range(0,101, 1):
        pred.ChangeDutyCycle(dc)
        sleep(0.01)
        print(dc)
      for dc in range(100, 0, -1):
        pred.ChangeDutyCycle(dc)
        sleep(0.01)
    if GPIO.input(b2) == GPIO.HIGH:
      pgreen = GPIO.PWM(green, f)
      pgreen.start(0)
      for dc in range(0, 101, 1):
        pgreen.ChangeDutyCycle(dc)
        sleep(0.01)
      for dc in range(100, 0, -1):
        pgreen.ChangeDutyCycle(dc)
        sleep(0.01)
    pred.stop()
    pgreen.stop()


  GPIO.add_event_detect(b1, GPIO.RISING, callback=myCallback,
bouncetime=200)
  GPIO.add_event_detect(b2, GPIO.RISING, callback=myCallback,
bouncetime=200)
  while True:
    pwm = GPIO.PWM(red, f) 
    pwm.start (dc)
    
    while 1:
      for dc in range(101): # loop duty cycle from 0 to 100
        pwm.ChangeDutyCycle(dc) # set duty cycle
        sleep(0.01) # sleep 10 ms


except KeyboardInterrupt: # stop gracefully on ctrl-C
  print("\nExiting")
except Exception as e: # catch all other errors
  print('/n',e)
pwm.stop()
GPIO.cleanup()
#switch 1 pressed