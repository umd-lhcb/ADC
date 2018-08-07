# Code for fire alarm leak sensor
# Written by Jorge Ramirez Ortiz
# Last edit: Tue Jul 31, 2018 at 13:50 PM -0400

 # nominal: no water means circuit is open & BCM 17 is LOW
 # leak detected: leak sensor closes, becomes 2Mohm resistor & BCM 17 is HIGH


import RPi.GPIO as GPIO
import time

 # set up
InputBCM = 17
GPIO.setmode(GPIO.BCM)  # use BCM pin system
GPIO.setup(InputBCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # setup pin w/ pullup


 # this method will be called if BCM 17 is HIGH (i.e. circuit closed)
def sound_the_alarm(channel):
    if GPIO.input(channel) == GPIO.HIGH:
        print('Leak! Leak!')
        time.sleep(0.01)


 # use event detect to monitor BCM17
GPIO.add_event_detect(InputBCM, GPIO.BOTH, callback=sound_the_alarm,
    bouncetime=100)

 # add_event_detect runs as a separate thread that waits for the pin to
 # change states, and when it does, it executes sound_the_alarm


try:
     # keep script open with a way to exit
    message = input('\nEnter Any Key to Exit.\n')

finally:
    GPIO.cleanup()

print("Exiting")