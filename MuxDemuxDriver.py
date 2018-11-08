"""
4051 Driver

Drives a 4051 Shift Register. 
© Keegan Crankshaw 2018

TODO: Add support for PWM pins

"""

import RPi.GPIO as GPIO
import itertools

class MuxDemux:
    
    def __init__(self, S0Pin, S1Pin, S2Pin, InOut=None, InOutPin=None, values):
    """
    Creates a 4051 object, in either input or output mode
    The input or output pin is specfied by InOutPin
    If InOut is asserted high or low by default in the circuit, set inout = ""
    """
        # assign pins
        self.S0 = S0Pin
        self.S1 = S0Pin
        self.S2 = S0Pin
        self.Z = InOutPin
        
        self.mode = InOut
        
        GPIO.setup(self.S0, GPIO.OUT)
        GPIO.setup(self.S1, GPIO.OUT)
        GPIO.setup(self.S2, GPIO.OUT)
        
        if (self.mode == "Out"):
            GPIO.setup(InOutPin, GPIO.OUT)
            self.values = [1]*8
        elif (self.mode = "In"): 
            GPIO.setup(InOutPin, GPIO.IN)
            self.values = []
            
            
    def iterate_all():
    """
    In IN mode, iterate_all iterates over each pin, taking in a digital value into the VALUES array
    In OUT mode, iterate_all writes the values to 
    """
    if InOut == "Out"
        for i in itertools.product([GPIO.LOW,GPIO.HIGH],repeat=3):
            # set the switches
            GPIO.output(self.S0Pin, i[0])
			GPIO.output(self.S1Pin, i[1])
			GPIO.output(self.S2Pin, i[2])
            
            # sleep to ensure signal propogation
            time.sleep(0.00001)
            
            # read or write data if necessary
            switch (self.mode) {
                case None: break
                case "Out": GPIO.output(self.Z, self.values[int(i)]
                case "In" self.values[int(i)] = GPIO.input(self.Z)
            }
            
    def POST():
    """
    TODO
    POST - Power on self test
    Simply iterates over each pin,
    """
        pass
            
            
if "__name__" == "__main__":
    try:
        while True:
            POST()
            
    except KeyboardInterrupt:
        GPIO.Close()
        print("Exiting")
            
        
        