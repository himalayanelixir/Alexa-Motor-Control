import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

Active= 9
Forward= 10
Backward= 11

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()
GPIO.setup(Active, GPIO.OUT)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)


GPIO.output(Active, True)
GPIO.output(Backward, True)
GPIO.output(Forward, False)
time.sleep(2)

GPIO.output(Active, True)
GPIO.output(Backward, False)
GPIO.output(Forward, False)
time.sleep(2)

GPIO.output(Active, True)
GPIO.output(Backward, False)
GPIO.output(Forward, True)
time.sleep(2)

GPIO.cleanup()