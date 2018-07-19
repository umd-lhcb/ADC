#!/usr/bin/env python
# Author: Jorge Ramirez
# Last Change: Thu Jul 12, 2018 at 04:56 PM -0400

import threading
import time
# FIXME: use pathlib instead of os.path---it's a newer lib with nicer features.
import os.path

# FIXME: don't use global variables---these should be configurable
# delay = 1  # 0.75 second delay between prints
# default_path = '/sys/bus/w1/devices'


# Detect how many sensors there are start 1 thread for each sensor
# FIXME: need implementation
def get_total_sensor_num(path):
    pass


class ThermThread(threading.Thread):
    '''
    each thermThread initializes w/ "ThreadID" which will be integer used as
    identifier "name" which will be therm serial.
    '''
    def __init__(self,
                 thread_id, sensor, *args,
                 delay=1, default_path='/sys/bus/w1/devices', **kwargs):
        self.thread_id = thread_id
        self.sensor = sensor

        self.delay = delay
        self.default_path = default_path

        super().__init__(self, *args, **kwargs)

    # default run will be to announce start print sensor name & temperature
    # continuously
    def run(self):
        print(("Starting Thread " + str(self.threadID) +
        " sensor " + self.sensor))
        while True:
            temp = self.get_therm(self.sensor)
            self.print_therm(self.sensor, temp, self.thread_id)

    def get_therm(self):
        newpath = os.path.join(self.default_path, "28-000009" + self.sensor,
        'w1_slave')

        # open file, copy all contents, close file
        # FIXME: use 'with'
        temp_file = open(newpath, 'r')
        contents = temp_file.readlines()
        temp_file.close()
        time.sleep(self.delay)

        # extract temperature
        temp_output = contents[1].find('t=')  # look for temp inside file
        temp_string = contents[1].strip()[temp_output + 2:]  # strip temp out
        temp_c = (float(temp_string) / 1000.0 * 9 / 5.0) + 32.0

        return temp_c

    @staticmethod
    def print_therm(sensor, data, thread_id):
        print("Sensor {} ({}) detects {}".format(thread_id, sensor, data))


if __name__ == '__main__':
    # FIXME: non-idomaitc implementation. Use a for loop.
    # create new threads
    thread1 = ThermThread(1, "8d0cbe")
    thread2 = ThermThread(2, "8d62d7")
    thread3 = ThermThread(3, "8d8197")
    thread4 = ThermThread(4, "8d94eb")
    thread5 = ThermThread(5, "8dd2b8")
    thread6 = ThermThread(6, "8e7ed7")
    thread7 = ThermThread(7, "8f007f")
    thread8 = ThermThread(8, "8fd7e3")
    thread9 = ThermThread(9, "9049c6")
    # start new threads
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread7.start()
    thread8.start()
    thread9.start()

    # FIXME: need to wait for sensor threads to join in the end
    thread1.join()  # etc...
