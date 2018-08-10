# !/usr/bin/env python
# Author: Jorge Ramirez
# Last Change: Fri Aug 10, 2018 at 9:07 AM -0400

from pathlib import Path
import threading
import time


def detect_sensors():
     # Detect how many sensors there are
    sensor_dir = "/sys/bus/w1/devices/"  # expected location of sensors
    scandir = Path(sensor_dir)  # set directory to be scanned
    sensorfolders = []  # save sensor folders in here

    for item in scandir.iterdir():
        if item.is_dir() and str(item.stem)[:8] == '28-00000':
            sensorfolders.append(item)

    return sensorfolders


def give_sensor_path(index):
    return detect_sensors().sensorfolders[index]

def give_sensor_serial(index):
    return str(detect_sensors()[index].stem)[8:]


def list_all_sensors():
    for x in range(len(detect_sensors())):
        print((give_sensor_serial(x)))


class ThermalThread(threading.Thread):

 # newthread = ThermalThread(thread_id, sensor serial #, delay (seconds))

     # default initialization
    def __init__(self, thread_id, sensor, delay, *args, **kwargs):
        self.thread_id = thread_id
        self.sensor = sensor

        if self.delay is None:
            self.delay = 1
        else:
            self.delay = self.delay

        super(ThermalThread, self, *args, **kwargs).__init__()

     # thread announces itself
    def announce(self):
        print(("Starting: (Thread " + str(self.thread_id) + ") (" +
        self.sensor + ")"))

    def extract_therm(self):
        path = give_sensor_path(self.thread_id)
             # open file, copy all contents, extract data
            with open(newpath, 'r') as file:
                    contents = file.readlines()
                    time.sleep(self.delay)
                     # extract raw data into variable "temp_string"
                    temp_output = contents[1].find('t=')
                    temp_string = contents[1].strip()[temp_output + 2:]
            return temp_string

