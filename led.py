from flask import Flask
from flask_ask import Ask, statement
import RPi.GPIO as GPIO
import time
 
app = Flask(__name__)
ask = Ask(app, '/')
 
@ask.intent('LedIntent')
def led(direction):
  #if color.lower() not in pins.keys():
  #  return statement("I don't have {} light".format(color)) 
  print ('Direction:', direction)
  if direction == 'up':
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(10,GPIO.HIGH)
    GPIO.output(11,GPIO.LOW)
    time.sleep(10)
    GPIO.output(9,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    return statement('Moving the motor {} '.format(direction))
  elif direction == 'down':
    GPIO.output(9,GPIO.HIGH)
    GPIO.output(10,GPIO.LOW)
    GPIO.output(11,GPIO.HIGH)
    time.sleep(10)
    GPIO.output(9,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    return statement('Moving the motor {} '.format(direction))
  else:
    GPIO.output(9,GPIO.LOW)
    GPIO.output(10,GPIO.LOW)
    GPIO.output(11,GPIO.LOW)
    return statement('Invalid Direction')
  
 
if __name__ == '__main__':
  try:
    GPIO.setmode(GPIO.BCM)
    pins = {9,10,11}
    for pin in pins: 
      GPIO.setup(pin, GPIO.OUT)
    app.run(debug=True)
  finally:
    GPIO.cleanup()