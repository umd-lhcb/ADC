
import RPi.GPIO as GPIO
import time

 # set up
InputBCM = 17
GPIO.setmode(GPIO.BCM)  # use BCM pin system
GPIO.setup(InputBCM, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # setup pin w/ pullup


while True:
    try:
        time.sleep(0.1)
        print(GPIO.input(InputBCM))
    except KeyboardInterrupt:
        GPIO.cleanup()
        break
