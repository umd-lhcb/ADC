__author__ = 'rohanrajagopalan'
#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
# S0-3 => Bit 1-4 (11, 12, 13, 15)
pins = [11, 12, 13, 15, 16, 18, 19]
s_x=pins[:4]

run = int(input('Runs: '))

num = 0
count = 0
t = .5
x = 0

while (count < run):
        count = count + 1
        print str('\n\nRun ' + str(count))
        while (num < 16):
                bin = [int(x) for x in list('{0:04}'.format(int('{0:0b}'.format(num))))]
                bin.reverse()
                print "BB Channel " + str(num)
                for i in s_x:
                    GPIO.setup(i, GPIO.OUT)
                    GPIO.output(i,bin[pins.index(i)])
                    print "Bit " + str(pins.index(i) + 1)
                time.sleep(t) #time delay between S3 and Vout only 35 ns
                num = num + 1
        num = 0                

print "\nDone"
GPIO.cleanup()
