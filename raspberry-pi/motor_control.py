#!/usr/bin/python3
# Copyright 2020 Harlen Bains
# linted using pylint
# formatted using black
"""This script runs on a Raspberry Pi and controls a Pololu G2 High-Power Motor
Driver 24v13 using the Raspberry Pi's GPIO pins.
"""

import sys
import time
from threading import Thread
from flask import Flask  # pylint: disable=import-error
from flask_ask import Ask, statement  # pylint: disable=import-error
import RPi.GPIO as GPIO  # pylint: disable=import-error


def moveup():
    """Set GPIO pins to tell the motor driver to move the furniture up wait for
    30 seconds and then and then stop.
    """
    global CURRENTLY_RUNNING
    CURRENTLY_RUNNING = 1
    GPIO.output(PINS[0], GPIO.HIGH)
    GPIO.output(PINS[1], GPIO.HIGH)
    GPIO.output(PINS[2], GPIO.HIGH)
    time.sleep(30)
    GPIO.output(PINS[0], GPIO.LOW)
    GPIO.output(PINS[1], GPIO.LOW)
    GPIO.output(PINS[2], GPIO.LOW)
    CURRENTLY_RUNNING = 0
    sys.exit()


def movedown():
    """Set GPIO pins to tell the motor driver to move the furniture down wait
    for 30 seconds and then and then stop.
    """
    global CURRENTLY_RUNNING
    CURRENTLY_RUNNING = 1
    GPIO.output(PINS[0], GPIO.HIGH)
    GPIO.output(PINS[1], GPIO.LOW)
    GPIO.output(PINS[2], GPIO.HIGH)
    time.sleep(30)
    GPIO.output(PINS[0], GPIO.LOW)
    GPIO.output(PINS[1], GPIO.LOW)
    GPIO.output(PINS[2], GPIO.LOW)
    CURRENTLY_RUNNING = 0
    sys.exit()


@ASK.intent("LedIntent")
def led(direction):
    """Get message from Alexa service with the direction we want to move the
    furniture and execute the command. If the furniture is currently moving or
    invalid command is sent send error statement back to Alexa.

    Args:
      direction: Direction we want to move the furniture

    Returns:
      Returns a response statement according to the state of the furniture
    """
    print("Direction:", direction)
    if CURRENTLY_RUNNING == 0:
        if direction == "up":
            thread = Thread(target=moveup)
            thread.start()
            response = "The couch is now moving {} ".format(direction)
        elif direction == "down":
            thread = Thread(target=movedown)
            thread.start()
            response = "The couch is now moving {} ".format(direction)
        else:
            GPIO.output(PINS[0], GPIO.LOW)
            GPIO.output(PINS[1], GPIO.LOW)
            GPIO.output(PINS[2], GPIO.LOW)
            response = "Invalid Direction"
    else:
        response = "The couch is currently moving please try again in a few moments"
    return statement(response)


APP = Flask(__name__)
ASK = Ask(APP, "/")
CURRENTLY_RUNNING = 0
GPIO.setmode(GPIO.BCM)
PINS = (9, 10, 11)

if __name__ == "__main__":
    try:
        for pin in PINS:
            GPIO.setup(pin, GPIO.OUT)
        APP.run(debug=True)
    finally:
        GPIO.cleanup()
