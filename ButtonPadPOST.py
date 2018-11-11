import RPi.GPIO as GPIO
import RGBDriver
import MuxDemuxDriver
import time

GPIO.setmode(GPIO.BOARD)

# create the 4051 object
m = MuxDemuxDriver.MuxDemux(36,38,40)

# Create the LEDs
LED = RGBDriver.RGB(37,33,31)

colours = [[0,0,100],[0,100,0],[100,0,0],[100,100,0],[0,100,100],[100,0,100],[100,100,100],[0,0,0]]

def POSTSingleColors():
    LED.changeColour([100,0,0])
    m.iterate_all(0.1)
    LED.changeColour([0,100,0])
    m.iterate_all(0.1)
    LED.changeColour([0,0,100])
    m.iterate_all(0.1)

def POSTAllSame():
    LED.changeColour([100,50,25])
    m.iterate_all()

def POSTDifferent():
    count = 0
    while True:
        m.next()
        LED.changeColour(colours[count])
        count = 0 if count == 7 else count+1

if __name__ == "__main__":
    try:
        while True:
            POSTDifferent()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nExiting")
