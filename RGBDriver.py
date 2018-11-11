"""
RGB LED Driver

File written to drive an RGB LED 
© Keegan Crankshaw 2018

"""

import RPi.GPIO as GPIO
import time
import RGBColours

class RGB:

    def __init__(self, RPin, GPin, BPin):
        """
        Method creates an RGB object using pins R, G and B out
        Colors are set all to high
        """
        self.RPin = RPin
        self.GPin = GPin
        self.BPin = BPin
        self.colours = [[100]*3];

        GPIO.setup(self.RPin, GPIO.OUT)
        GPIO.setup(self.GPin, GPIO.OUT)
        GPIO.setup(self.BPin, GPIO.OUT)

        self.freq = 100000

        self.RED = GPIO.PWM(self.RPin, self.freq)
        self.BLUE = GPIO.PWM(self.BPin, self.freq)
        self.GREEN = GPIO.PWM(self.GPin, self.freq)

        self.RED.start(0)
        self.GREEN.start(0)
        self.BLUE.start(0)

    def changeColour(self, RGBValues):
        self.colours = RGBValues
        self.RED.ChangeDutyCycle(self.colours[0])
        self.GREEN.ChangeDutyCycle(self.colours[1])
        self.BLUE.ChangeDutyCycle(self.colours[2])

    def POST(self):
        for c in RGBColours.Colours:
            print(c)
            self.changeColour(RGBColours.Colours[c])
            time.sleep(0.2)
        return
        self.changeColour([100,0,0])
        time.sleep(0.5)
        self.changeColour([0,100,0])
        time.sleep(0.5)
        self.changeColour([0,0,100])
        time.sleep(0.5)
        for r in range(0,100,10):
            for g in range(0,100,10):
                for b in range(0,100,10):
                    self.changeColour([r,g,b])
                    time.sleep(0.05)



if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BOARD)
        led = RGB(37,33,31)
        print("Starting RGB POST")
        #while True:
        led.POST()
        GPIO.cleanup()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nExiting")
