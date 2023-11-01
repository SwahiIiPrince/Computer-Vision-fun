import os
import RPi.GPIO as GPIO
import time


def do_green():
   GPIO.setmode(GPIO.BOARD)
   ledPin = 31
   GPIO.setup(ledPin, GPIO.OUT, initial = GPIO.HIGH)
   GPIO.output(ledPin, GPIO.LOW)
   time.sleep(0.01)
   GPIO.output(ledPin, GPIO.HIGH)
   GPIO.cleanup()
