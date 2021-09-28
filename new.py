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

pwm2 = GPIO.PWM(blue, 100)# create PWM object @ 100 Hz
pwm1 = GPIO.PWM(green, 100) # create PWM object @ 100 Hz

def fade(self):          

  try:
    if GPIO.input(inBlue) == GPIO.HIGH:
      pwm2.start(0) 
      for dc in range(100, 0 , -1): 
        pwm2.ChangeDutyCycle(dc)   
        sleep(0.01)               
      for dc in range(0, 100, 1):  
        pwm2.ChangeDutyCycle(dc)  
        sleep(0.01) 
    if GPIO.input(inGreen) == GPIO.HIGH:
      pwm1.start(0) 
      for dc in range(100, 0 , -1): 
        pwm1.ChangeDutyCycle(dc)   
        sleep(0.01)               
      for dc in range(0, 100, 1):  
        pwm1.ChangeDutyCycle(dc)  
        sleep(0.01)


  except KeyboardInterrupt:       
    print('\nExiting')

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


GPIO.add_event_detect(inGreen, GPIO.RISING, callback=fade, bouncetime=200) 
GPIO.add_event_detect(inBlue, GPIO.RISING, callback=fade, bouncetime=200) 

while True:                
  GPIO.output(red, 0)# set output to 0
  sleep(0.5)# wait 0.5 sec
  GPIO.output(red, 1)# set output to 3.3V
  sleep(0.5)

pwm2.stop()
pwm1.stop()
GPIO.cleanup()

# GPIO.add_event_detect(inGreen, GPIO.RISING, callback=fade(), bouncetime=200) 
# GPIO.add_event_detect(inBlue, GPIO.RISING, callback=fade(), bouncetime=200) 
# while True:                
#   GPIO.output(red, 0)# set output to 0
#   sleep(0.5)# wait 0.5 sec
#   GPIO.output(red, 1)# set output to 3.3V
#   sleep(0.5)