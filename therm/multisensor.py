# code goes here
# Author: Jorge Ramirez
# Last Edit - July 12th, 2018

import threading
import time
import random
import os.path

delay = 1  # 0.75 second delay between prints

defaultpath = '/sys/bus/w1/devices'

#detect how many sensors there are
#start 1 thread for each sensor

#begin main loop
#print array


class thermThread (threading.Thread):

    #each thermThread initializes w/
    #"threadID" which will be integer used as identifier
    #"name" which will be therm serial #

    def __init__(self, threadID, sensor):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.sensor = sensor

    #default run will be to announce start
    #print sensor name & temperature continuously

    def run(self):
        print(("Starting Thread " + str(self.threadID) +
        " sensor " + self.sensor))
        while True:  # loop
            temp = get_therm(self.sensor)
            print_therm(self.sensor, temp, self.threadID)


#function used inside thermThread to open temp and save to variable
def get_therm(sensorName):
    newpath = os.path.join(defaultpath, "28-000009" + sensorName,
    'w1_slave')

    #open file, copy all contents, close file
    temp_file = open(newpath, 'r')
    contents = temp_file.readlines()
    temp_file.close()
    time.sleep(delay)

    #extract temperature
    temp_output = contents[1].find('t=')  # look for temp inside file
    temp_string = contents[1].strip()[temp_output + 2:]  # strip temp out
    temp_c = (float(temp_string) / 1000.0 * 9 / 5.0) + 32.0

    return temp_c


#function used inside thermThread to print temp
def print_therm(sensorName, data, threadID):
    print(("Sensor " + str(threadID) + " (" + sensorName + ") detects "
    + str(data)))
    #time.sleep(delay)


#create new threads

thread1 = thermThread(1, "8d0cbe")
thread2 = thermThread(2, "8d62d7")
thread3 = thermThread(3, "8d8197")
thread4 = thermThread(4, "8d94eb")
thread5 = thermThread(5, "8dd2b8")
thread6 = thermThread(6, "8e7ed7")
thread7 = thermThread(7, "8f007f")
thread8 = thermThread(8, "8fd7e3")
thread9 = thermThread(9, "9049c6")

#start new threads

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread5.start()
thread6.start()
thread7.start()
thread8.start()
thread9.start()
