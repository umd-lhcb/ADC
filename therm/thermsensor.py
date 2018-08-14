# !/usr/bin/env python
# Author: Jorge Ramirez
# Last Change: Fri Aug 10, 2018 at 9:07 AM -0400

from pathlib import Path
import threading
import time
import sys

sensorfolders = []  # save sensor folders in here


def detect_sensors():
     # Detect how many sensors there are
    sensor_dir = "/sys/bus/w1/devices/"  # expected location of sensors
    scandir = Path(sensor_dir)  # set directory to be scanned

    print('\nDetecting sensors and adding to list...')
    for item in scandir.iterdir():
        if item.is_dir() and str(item.stem)[:8] == '28-00000':
            sensorfolders.append(item)
            print(('sensor ' + str(item.stem)[8:] + ' appended.'))
    return sensorfolders


def give_sensor_path(index):
    return sensorfolders[index]


def give_sensor_serial(index):
    return str(sensorfolders[index].stem)[8:]


def list_all_sensors():
    print((str(len(sensorfolders)) + ' sensors found:'))
    for item in range(len(sensorfolders)):
        print((give_sensor_serial(item)))


class ThermalThread(threading.Thread):

 # newthread = ThermalThread(thread_id, sensor serial #, delay (seconds))
    def __init__(self, thread_id, sensor, delay, *args, **kwargs):
        self.thread_id = thread_id
        self.sensor = sensor
        self.delay = delay

        if self.delay is None:
            self.delay = 1
        else:
            self.delay = self.delay

        super(ThermalThread, self, *args, **kwargs).__init__()

     # thread announces itself
    def announce(self):
        print(("Starting: (Thread " + str(self.thread_id) + ") (" +
        str(self.sensor) + ")"))

    def extract_therm(self):
        sensordir = give_sensor_path(self.thread_id)  # get directory of sensor
        path = sensordir / 'w1_slave'  # append file to path

             # open file, copy all contents, extract data
        with path.open() as f:
                contents = f.readlines()
                time.sleep(self.delay)
                 # extract raw data into variable "temp_string"
                temp_output = contents[1].find('t=')
                temp_string = contents[1].strip()[temp_output + 2:]

        return (int(temp_string) / 1000)  # add decimal point to data

    @staticmethod
    def print_therm(self, sensor, data, thread_id):
        serial = give_sensor_serial(thread_id)
        print(("Sensor {} ({}) detects {}".format(thread_id, serial, data)))

    def run(self):
        self.announce()  # announce init
        while True:
            data = str(self.extract_therm())  # extract
            self.print_therm(self, self.sensor, data, self.thread_id)  # print


 # main code

if __name__ == '__main__':

     # detect sensors and assign threads
    detect_sensors()
    thread_dir = ["Thread" + str(x + 1) for x in range(len(sensorfolders))]

     # create new threads
    for i in range(len(sensorfolders)):
        thread_dir[i] = ThermalThread(i, sensorfolders[i],
        int(sys.argv[1]))  # delay is input via terminal, default is 1s

     # start new threads once all have been initialized
    for i in range(len(sensorfolders)):
        thread_dir[i].start()
