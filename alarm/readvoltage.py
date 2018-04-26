#!/usr/bin/env python
#
# Last Change: Thu Apr 26, 2018 at 02:06 PM -0400

import RPi.GPIO as GPIO


class AlarmSetup(object):
    def __init__(self, ch):
        self.ch = ch

        GPIO.setmode(GPIO.BOARD)
        # To quote from:
        # https://www.raspberrypi.org/forums/viewtopic.php?t=87292
        #   The pull-up/downs supply some voltage so that the GPIO will have a
        #   defined value UNTIL overridden by a stronger force.
        #   You should set a pull-down (to 0) when you expect the stronger force
        #   to pull it up to 1.
        #   You should set a pull-up (to 1) when you expect the stronger force
        #   to pull it down to 0.
        GPIO.setup(self.ch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def cleanup(self):
        GPIO.cleanup()

    def read_channel(self):
        return GPIO.input(self.ch)


if __name__ == '__main__':
    import sys.argv

    alarm = AlarmSetup(ch=int(sys.argv[1]))

    while True:
        try:
            if alarm.read_channel() == 1:
                print('Fire!')
        except KeyboardInterrupt:
            break

    alarm.cleanup()
