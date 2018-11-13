#!/usr/bin/env python3

"""
RGB LED Driver

File written to drive an RGB LED 
Keegan Crankshaw 2018

"""

import RPi.GPIO as GPIO
import time
import itertools

class RGB:

    def __init__(self, RPin, GPin, BPin):
        """
        Method creates an RGB object using pins R, G and B out
        Colors are set all to high
        """
        self.RPin = RPin
        self.GPin = GPin
        self.BPin = BPin
        self.colours = [1,1,1];

        GPIO.setup(self.RPin, GPIO.OUT)
        GPIO.setup(self.GPin, GPIO.OUT)
        GPIO.setup(self.BPin, GPIO.OUT)


    def changeColour(self, RGBValues):
        self.colours = RGBValues
        GPIO.output(self.RPin, self.colours[0])
        GPIO.output(self.GPin, self.colours[1])
        GPIO.output(self.BPin, self.colours[2])


    def POST(self):
        for i in itertools.product([GPIO.LOW, GPIO.HIGH],repeat=3):
            print(i)
            self.changeColour(i)
            time.sleep(0.5)

if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BOARD)
        led = RGB(37,35,33)
        print("Starting RGB POST")
        while True:
            led.POST()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nExiting")
