"""
RGB LED Driver

File written to drive an RGB LED 
© Keegan Crankshaw 2018

"""


class RGB:
    
    def __init__(self, RPin, GPin, BPin):
    """
    Method creates an RGB object using pins R, G and B out
    Colors are set all to high
    """
        self.R = RPin
        self.G = GPin
        self.B = BPin
        colours = [[100]*3]*8;
        
        
    def POST():
        # run a POST 
        

if "__name__" == "__main__":
    try:
        while True:
            POST()
            
    except KeyboardInterrupt:
        GPIO.Close()
        print("Exiting")