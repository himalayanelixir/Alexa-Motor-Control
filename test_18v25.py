import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# setup pins as output
GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

for x in range(6):
    print("Loop: ", x)
    # move forward
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(10,GPIO.HIGH)
    time.sleep(30)
    #set off
    #GPIO.output(9,GPIO.LOW)
    #GPIO.output(10,GPIO.LOW)
    #time.sleep(10)
    # move backwards
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(10,GPIO.LOW)
    time.sleep(30)
    #set off
    #GPIO.output(9,GPIO.LOW)
    #GPIO.output(10,GPIO.LOW)
    #time.sleep(10)

#set off
GPIO.output(9,GPIO.LOW)
GPIO.output(10,GPIO.LOW)
GPIO.cleanup()