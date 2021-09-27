#lab 2 ENME441


# import RPi.GPIO as GPIO
# from time import sleep # import time.sleep()
# GPIO.setmode(GPIO.BCM)# use BCM port numbering
# p = 4                      # pin number
# GPIO.setup(p, GPIO.OUT)# assign the pin as output
# while True:                
#   GPIO.output(p, 0)# set output to 0
#   sleep(0.5)# wait 0.5 sec
#   GPIO.output(p, 1)# set output to 3.3V
#   sleep(0.5)

#green LED1
#Blue LED2
#Red LED3
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




# import RPi.GPIO as GPIO 
# from time import sleep
# GPIO.setmode(GPIO.BCM)
# p = 4
# GPIO.setup(p, GPIO.OUT)
# pwm = GPIO.PWM(p, 100)          
# try:
#   pwm.start(0)                  
#   while 1:
#     for dc in range(101):       
#       pwm.ChangeDutyCycle(dc)   
#       sleep(0.01)               
# except KeyboardInterrupt:       
#   print('\nExiting')

# pwm.stop()
# GPIO.cleanup()

