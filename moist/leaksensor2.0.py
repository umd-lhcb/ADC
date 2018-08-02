                  #!/usr/bin/env python
#
# Last Change: Thu Apr 26, 2018 at 02:08 PM -0400

import RPi.GPIO as GPIO
import time
import sys

InputBCM = 17


class AlarmSetup(object):
    def __init__(self, ch):
        self.ch = ch

        # Use the Board numbering
        GPIO.setmode(GPIO.BOARD)

        # To quote from:
        # https://www.raspberrypi.org/forums/viewtopic.php?t=87292
        #   The pull-up/downs supply some voltage so that the GPIO will have a
        #   defined value UNTIL overridden by a stronger force.
        #   You should set a pull-down (to 0) when you expect the stronger force
        #   to pull it up to 1.
        #   You should set a pull-up (to 1) when you expect the stronger force
        #   to pull it down to 0.
        #   Maybe we don't need this parameter after all.
        #GPIO.setup(self.ch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.ch, GPIO.IN)

    def cleanup(self):
        GPIO.cleanup()

    def read_channel(self):
        return GPIO.input(self.ch)


if __name__ == '__main__':

    # alarm = AlarmSetup(ch=int(sys.argv[1]))
    alarm = WaterAlarm(InputBCM)
    while True:
        try:
            if alarm.read_channel() == 0:
                print('Fire!')
                time.sleep(0.25)
        except KeyboardInterrupt:
            break

    alarm.cleanup()
