#!/usr/bin/env python
#
# Authors: Jorge Ramirez Ortiz, Yipeng Sun
# Last Change: Wed Aug 15, 2018 at 06:05 PM -0400


import RPi.GPIO as GPIO
import sys

from threading import Thread, Event
from time import sleep


class WaterAlarm(Thread):
    def __init__(self, stop_event, *args,
                 ch=9, interval=0.01, alarm_threshold=2, **kwargs):
        self.stop_event = stop_event
        self.ch = ch
        self.interval = interval
        self.alarm_threshold = alarm_threshold

        # 'leak_counter' variable can be used to guard against false alarms.
        #
        # This class will monitor the input pin for a HIGH. It is default LOW
        # due to an internal pulldown resistor. It will probe every 0.1 seconds,
        # and if it detects a leak, then the 'leak_counter' variable will
        # increase by one.
        #
        # It seems as if 1 hit to leak_counter can be safely ignored, even tiny
        # drops that run across the sensor trigger the sensor at least twice.
        #
        # Anything more than 5 hits is a major leak (the sensor is in a puddle
        # of water)
        self.leak_counter = 0

        GPIO.setmode(GPIO.BOARD)

        # nominal: no water means circuit is open & BCM 17 is LOW due to
        #          PULLDOWN
        # water detected: leak sensor closes, becomes 2M ohm resistor & BCM 17
        #                 is HIGH
        GPIO.setup(self.ch, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)  # activate pin

        super().__init__(*args, **kwargs)

    def run(self):
        while not self.stop_event.wait(self.interval):
            if self.read_channel() == 1:
                self.leak_counter += 1
                if self.leak_counter >= self.alarm_threshold:
                    self.alarm()

    def cleanup(self):
        GPIO.cleanup(self.ch)
        self.join()

    def read_channel(self):
        return GPIO.input(self.ch)

    def alarm(self):
        print('Leak!!!')


if __name__ == '__main__':  # ensure that script is being run from terminal
    stop_event = Event()

    print("Initializing water leak detector...")
    alarm = WaterAlarm(stop_event, ch=int(sys.argv[1]))
    alarm.start()

    while True:
        try:
            sleep(0.1)
        except KeyboardInterrupt:
            stop_event.set()

    alarm.cleanup()
