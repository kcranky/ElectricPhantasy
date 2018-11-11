"""
4051 Driver

Drives a 4051 Shift Register.
Keegan Crankshaw 2018

TODO: Add support for PWM pins

"""
import RPi.GPIO as GPIO
import itertools
import time

class MuxDemux:

    def __init__(self, S0Pin, S1Pin, S2Pin, values=[], InOut=None, InOutPin=None):
        """
        Creates a 4051 object, in either input or output mode
        The input or output pin is specfied by InOutPin
        If InOut is asserted high or low by default in the circuit, set inout = ''
        """
        # assign pins
        self.S0 = S0Pin
        self.S1 = S1Pin
        self.S2 = S2Pin
        self.Z = InOutPin

        self.mode = InOut

        GPIO.setup(self.S0, GPIO.OUT)
        GPIO.setup(self.S1, GPIO.OUT)
        GPIO.setup(self.S2, GPIO.OUT)

        if (self.mode == "Out"):
            GPIO.setup(InOutPin, GPIO.OUT)
            self.values = [1]*8
        elif (self.mode == "In"):
            GPIO.setup(InOutPin, GPIO.IN)
            self.values = []


    def iterate_all(self):
        """
        In IN mode, iterate_all iterates over each pin, taking in a digital value into the VALUES array
        In OUT mode, iterate_all writes the values to
        """
        if (InOut == "Out"):
            for i in itertools.product([GPIO.LOW,GPIO.HIGH],repeat=3):
                # set the switches
                GPIO.output(self.S0, i[0])
                GPIO.output(self.S1, i[1])
                GPIO.output(self.S2, i[2])

                # sleep to ensure signal propogation
                time.sleep(0.00001)

                # read or write data if necessary
                if (self.mode == "Out"):
                    GPIO.output(self.Z, self.values[int(i)])
                elif (self.mode == "In"):
                    self.values[int(i)] = GPIO.input(self.Z)


    def POST(self):
        """
        TODO
        POST - Power on self test
        Simply iterates over each pin
        Assumes an object is created using GPIO.BOARD on pins 36, 38 and 40
        """
        for i in itertools.product([GPIO.LOW,GPIO.HIGH],repeat=3):
            # set the switches
            GPIO.output(self.S0, i[0])
            GPIO.output(self.S1, i[1])
            GPIO.output(self.S2, i[2])
            # delay so effects are observable
            time.sleep(0.5)



if __name__ == "__main__":
    try:
        # set up the object
        GPIO.setmode(GPIO.BOARD)
        mux = MuxDemux(36,38,40)
        print("Starting POST for MuxDemuxDriver")
        print("Assumes Mux has Z connected high")
        print("Assumes connections to BOARD pins 36,38,40 for S0-S2")
        while True:
            mux.POST()

    except KeyboardInterrupt:
        GPIO.cleanup()
        print("\nExiting")

