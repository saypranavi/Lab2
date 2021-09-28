import RPi.GPIO as GPIO 
from time import sleep

GPIO.setmode(GPIO.BCM)
red = 26 #LED3 will blink
blue = 19 #LED2 will fade with button press
green = 13 #LED1 will fade with button press
f = 1     # frequency (Hz)
dc = 50   # duty cycle (%)
inBlue = 21 #button for blue
inGreen = 24 #button for green
GPIO.setup(red, GPIO.OUT) #set up LEDs as outputs
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(inBlue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #set up buttons as inputs
GPIO.setup(inGreen, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

pwm2 = GPIO.PWM(blue, 100)# create PWM object @ 100 Hz
pwm1 = GPIO.PWM(green, 100) # create PWM object @ 100 Hz
pwm1.start(100) #starts the blue LED as "off"
pwm2.start(100) #starts the green LED as "off"

def fade(self):     #callback function     
  try:
    if GPIO.input(inBlue) == GPIO.HIGH: #check if blue button pushed
      pwm2.start(100)  #if on fade all the way up
      for dc in range(100, 0 , -1): 
        pwm2.ChangeDutyCycle(dc)   
        sleep(0.01)               
      for dc in range(0, 100, 1):  #fade back down to "off"
        pwm2.ChangeDutyCycle(dc)  
        sleep(0.01) 
    if GPIO.input(inGreen) == GPIO.HIGH: #check if green button pushed
      pwm1.start(100) 
      for dc in range(100, 0 , -1): #if on fade all the way up
        pwm1.ChangeDutyCycle(dc)   
        sleep(0.01)               
      for dc in range(0, 100, 1):  #fade back down to "off"
        pwm1.ChangeDutyCycle(dc)  
        sleep(0.01)
  except KeyboardInterrupt:   #exit on ctrl c    
    print('\nExiting')
#callback function for each button detected
GPIO.add_event_detect(inGreen, GPIO.RISING, callback=fade, bouncetime=200) 
GPIO.add_event_detect(inBlue, GPIO.RISING, callback=fade, bouncetime=200) 
#Continuously blink the red light
while True:                
  GPIO.output(red, 0)# set output to 0
  sleep(0.5)# wait 0.5 sec
  GPIO.output(red, 1)# set output to 3.3V
  sleep(0.5)
#stop the LEDs without button and clean up
pwm2.stop()
pwm1.stop()
GPIO.cleanup()
