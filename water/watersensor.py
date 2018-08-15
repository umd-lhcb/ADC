#!/usr/bin/env python
#
# Authors: Jorge Ramirez Ortiz, Yipeng Sun
# Last Change: Wed Aug 15, 2018 at 03:37 PM -0400

# nominal: no water means circuit is open & BCM 17 is LOW due to PULLDOWN
# water detected: leak sensor closes, becomes 2Mohm resistor & BCM 17 is HIGH

import RPi.GPIO as GPIO
import time
import sys


class WaterAlarm(object):
    '''
    alarm.leakcounter variable can be used to guard against false alarms.

    This script will monitor the input pin for a HIGH. it is default LOW due to
    an internal pulldown resistor. it will probe every 0.1 seconds, and if it
    detects a leak, then the 'leakcounter' variable wil lincrease by one.

    It seems as if 1 hit to leakcounter can be safely ignored, even tiny drops
    that run across the sensor trigger the sensor at least twice.

    Anything more than 5 hits is a major leak (the sensor is in a puddle of
    water)

    '''
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


if __name__ == '__main__':  # ensure that script is being run from termianl
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
