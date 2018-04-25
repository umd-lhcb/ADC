#!/usr/bin/env python
#
# Last Change: Mon Feb 05, 2018 at 09:11 PM -0500

import RPi.GPIO as GPIO


def init():
    GPIO.setmode(GPIO.BOARD)


def cleanup():
    GPIO.cleanup()
