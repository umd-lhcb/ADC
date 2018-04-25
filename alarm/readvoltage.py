#!/usr/bin/env python
#
# Last Change: Wed Apr 25, 2018 at 05:56 PM -0400

import RPi.GPIO as GPIO


class AlarmSetup(object):
    ch1 = 14

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ch1, pull_up_down=GPIO.PUD_DOWN)

    def cleanup(self):
        GPIO.cleanup()

    def read_channels(self):
        return GPIO.input(self.ch1)


if __name__ == '__main__':
    from time import sleep

    alarm = AlarmSetup()

    while True:
        try:
            print(alarm.read_channels())
            sleep(0.01)
        except KeyboardInterrupt:
            break
