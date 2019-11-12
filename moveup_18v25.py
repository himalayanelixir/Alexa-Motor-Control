import sys
import time
import RPi.GPIO as GPIO

mode=GPIO.getmode()

#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

GPIO.setup(9, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)

GPIO.output(9,GPIO.HIGH)
GPIO.output(10,GPIO.HIGH)

time.sleep(30)
GPIO.output(9,GPIO.LOW)
GPIO.output(10,GPIO.LOW)

GPIO.cleanup()