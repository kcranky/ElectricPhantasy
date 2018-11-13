
import RPi.GPIO as GPIO
import RGBDriver
import MuxDemuxDriver
import time
import itertools

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
    m.next()
    while True:
        m.next()
        LED.changeColour(colours[count])
        count = 0 if count == 7 else count+1


def POSTSelf():
    count = 7
    while True:
         for i in itertools.product([GPIO.LOW,GPIO.HIGH],repeat=3):
            LED.RED.ChangeDutyCycle(colours[count][0])
            LED.GREEN.ChangeDutyCycle(colours[count][1])
            LED.BLUE.ChangeDutyCycle(colours[count][2])
            GPIO.output(m.S0, i[0])
            GPIO.output(m.S1, i[1])
            GPIO.output(m.S2, i[2])
            count = 0 if count == 7 else count +1
            for i in range(7500):
                pass


if __name__ == "__main__":
    try:
        POSTSelf()
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nExiting")
