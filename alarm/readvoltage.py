#!/usr/bin/env python
#
# Last Change: Wed Apr 25, 2018 at 05:56 PM -0400

import RPi.GPIO as GPIO


class AlarmSetup(object):
    def __init__(self, ch):
        self.ch = ch
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.ch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    def cleanup(self):
        GPIO.cleanup()

    def read_channel(self):
        return GPIO.input(self.ch)


if __name__ == '__main__':
    from time import sleep

    alarm = AlarmSetup(ch=29)

    while True:
        try:
            if alarm.read_channel() == 1:
                print('Fire!')
        except KeyboardInterrupt:
            break

    alarm.cleanup()
