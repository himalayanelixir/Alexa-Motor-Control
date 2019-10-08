import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()
GPIO.cleanup()

Active= 11
Forward= 13
Backward= 15


sleeptime = 15


GPIO.setmode(GPIO.BOARD)
GPIO.setup(Active, GPIO.OUT)
GPIO.setup(Forward, GPIO.OUT)
GPIO.setup(Backward, GPIO.OUT)