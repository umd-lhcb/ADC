# !/usr/bin/env python
# Author: Jorge Ramirez
# Last Change: Thu Jul 19, 2018 at 15:07 PM -0400

import threading
import time
 # FIXME: use pathlib instead of os.path---it's a newer lib with nicer features.
import os.path

 # list of current 9 sensors
sensor_dir = ["8d0cbe", "8d62d7", "8d8197", "8d94eb", "8dd2b8",
"8e7ed7", "8f007f", "8fd7e3", "9049c6"]

 # create directory of threads to be called
thread_dir = ["Thread" + str(x + 1) for x in range(9)]


 # FIXME: need implementation
def get_total_sensor_num(path):
     # Detect how many sensors there are & start 1 thread for each sensor
    pass


class ThermThread(threading.Thread):
    '''
    each thermThread initializes w/ "thread_id" which will be an integer used
    as identifier "n
    ame" which will be therm serial.
    '''
     # initialize thread with standard arguments
    def __init__(self,
        thread_id, sensor, *args,
        delay=1, default_path='/sys/bus/w1/devices', **kwargs):

        self.thread_id = thread_id
        self.sensor = sensor
        self.delay = delay
        self.default_path = default_path

        super(ThermThread, self, *args, **kwargs).__init__()

     # thread invited to introduce themselves
    def announce(self):
        print(("Starting: (Thread " + str(self.thread_id) + ") (" +
        self.sensor + ")"))

     # thread opens temperature file and then saves it as a string
    def extract_therm(self):
        newpath = os.path.join(self.default_path, "28-000009" + self.sensor,
        'w1_slave')
         # open file, copy all contents, extract data
        with open(newpath, 'r') as file:
                contents = file.readlines()
                time.sleep(self.delay)
                 # extract raw data into variable "temp_string"
                temp_output = contents[1].find('t=')
                temp_string = contents[1].strip()[temp_output + 2:]
        return temp_string

     # simple convert method. It will probably be removed. perhaps it will be
     # more beneficial to return the raw temp_string to the server process
    def convert_therm(self, sensor_num):
        fahrenheit = (float(sensor_num) / 1000.0 * 9 / 5.0) + 32.0
        return fahrenheit

    @staticmethod
    def print_therm(self, sensor, data, thread_id):
        print(("Sensor {} ({}) detects {}".format(thread_id, sensor, data)))


     # thread task: announce -> loop(extract -> convert -> print)
    def run(self):
        self.announce()  # announce
        while True:
            data = self.extract_therm()  # extract
            final = self.convert_therm(data)  # convert
            self.print_therm(self, self.sensor, final, self.thread_id)  # print


if __name__ == '__main__':
     # create new threads
    for i in range(len(sensor_dir)):
        thread_dir[i] = ThermThread(i, sensor_dir[i])  # (thread_id, sensor)

     # start new threads once all have been initialized
    for i in range(len(sensor_dir)):
        thread_dir[i].start()
