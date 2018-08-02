                  #!/usr/bin/env python
#
# Last Change: Thu Apr 26, 2018 at 02:08 PM -0400

import RPi.GPIO as GPIO
import time
import sys

InputBCM = 17


class WaterAlarm(object):
    def __init__(self, ch):
        self.ch = ch
        GPIO.setmode(GPIO.BCM)  # use BCM pin system
        GPIO.setup(InputBCM, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # activate pin

    def cleanup(self):
        GPIO.cleanup()

    def read_channel(self):
        return GPIO.input(self.ch)


if __name__ == '__main__':

    print('initializing WaterAlarm')
    # alarm = AlarmSetup(ch=int(sys.argv[1]))
    alarm = WaterAlarm(ch=InputBCM)
    counter = 0
    while True:
        try:
            if alarm.read_channel() == 0:
                print('Leak! ' + str(counter))
                time.sleep(0.01)
                counter += 1
        except KeyboardInterrupt:
            break

    alarm.cleanup()
