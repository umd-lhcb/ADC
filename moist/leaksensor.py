# Code for firealarm leak sensor
# Written by Jorge Ramirez Ortiz
# Last edit: Tue Aug 07, 2018 at 9:01 AM -0400

 # nominal: no water means circuit is open & BCM 17 is LOW
 # leak detected: leak sensor closes, becomes 2Mohm resistor & BCM 17 is HIGH

import RPi.GPIO as GPIO
import time
import sys


class WaterAlarm(object):

    def __init__(self, ch):
        self.ch = ch
        self.leakcounter = 0  # counter to see how long leak lasted
        GPIO.setmode(GPIO.BCM)  # use BCM pin system
        GPIO.setup(self.ch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # activate pin

    def cleanup(self):
        GPIO.cleanup(self.ch)

    def read_channel(self):
        return GPIO.input(self.ch)

    def hitcounter(self):
        self.leakcounter += 1
        return str(self.leakcounter)


if __name__ == '__main__':
    print('initializing WaterAlarm')
    alarm = WaterAlarm(ch=int(sys.argv[1]))  # init alarm w/ ch from terminal

    while True:
        try:
            if alarm.read_channel() == 1:
                time.sleep(0.1)
                print('Leak detected! (' + alarm.hitcounter() + ')')
        except KeyboardInterrupt:
            alarm.cleanup()
            break
