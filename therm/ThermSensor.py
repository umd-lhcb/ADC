#!/usr/bin/env python
#
# Authors: Jorge Ramirez, Yipeng Sun
# Last Change: Wed Aug 15, 2018 at 05:04 PM -0400

import logging
import sys

from pathlib import Path
from threading import Thread, Event

logger = logging.getLogger(__name__)


class ThermSensor(Thread):
    def __init__(self,
                 stop_event,
                 *args,
                 sensor=None, display_name=None, interval=5,
                 **kwargs):
        self.stop_event = stop_event
        self.sensor = sensor
        self.display_name = display_name
        self.interval = interval

        super().__init__(*args, **kwargs)

    def run(self):
        self.announce()

        while not self.stop_event.wait(self.interval):
            data = str(self.get())
            self.print_therm(self.sensor.stem, self.display_name, data)

    def get(self):
        with self.sensor.open() as f:
            contents = f.readlines()
            # extract raw data into variable "temp_string"
            temp_output = contents[1].find('t=')
            temp_string = contents[1].strip()[temp_output + 2:]

        return int(temp_string) / 1000  # add decimal point to data

    def cleanup(self):
        self.join()

    def announce(self):
        logger.info("Starting: read from {}, with a display name of {}".format(
            self.sensor.stem, self.display_name
        ))

    @staticmethod
    def print_therm(sensor_name, display_name, data):
        print(("Sensor {} (from file {}) detects {}".format(
            display_name, sensor_name, data)))


###########
# Helpers #
###########

def detect_sensors(sensor_dir="/sys/bus/w1/devices",
                   sensor_name_prefix='28-00000',
                   sensor_file_name='w1_slave'):
    scan_dir = Path(sensor_dir)  # set directory to be scanned
    sensor_list = []

    print('Detecting sensors and adding to list...')
    for item in scan_dir.iterdir():
        if item.is_dir() and item.stem[:8] == sensor_name_prefix:
            sensor = item / Path(sensor_file_name)
            sensor_list.append(sensor)
            print('sensor {} appended.'.format(sensor.stem))

    return sensor_list


def list_all_sensors(**kwargs):
    sensor_list = detect_sensors(**kwargs)

    for sensor in sensor_list:
        print("Detected the following sensor: {}".format(sensor.stem))


if __name__ == '__main__':
    # detect sensors and assign threads
    sensor_path = detect_sensors()
    sensor_list = []
    stop_event = Event()

    # create new threads
    for i in range(len(sensor_path)):
        sensor_list.append(
            ThermSensor(stop_event,
                        sensor=sensor_path[i], display_name=str(i),
                        interval=int(sys.argv[1])
                        ))

    # start new threads once all have been initialized
    for sensor in sensor_list:
        sensor.start()

    while True:
        try:
            pass
        except KeyboardInterrupt:
            stop_event.set()
            # cleanup in the end
            for sensor in sensor_list:
                sensor.cleanup()
