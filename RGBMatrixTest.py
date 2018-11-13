import RPi.GPIO as GPIO
import itertools
import time

# Define pins used
SW1 = 36
SW2 = 38
SW3 = 40

#colors = [[GPIO.HIGH,GPIO.HIGH,GPIO.HIGH],[GPIO.LOW,GPIO.HIGH,GPIO.LOW],[GPIO.HIGH,GPIO.LOW,GPIO.LOW]] #, [0,0,0], [0,0,0], [0,0,0],[0,0,0],[0,0,0]]
colors = [[56,27,100],[0,100,0],[100,0,0],[100,0,0],[0,100,0],[0,0,100],[100,0,0],[0,100,0]]
R = 33
G = 31
B = 37

RDC = 3
GDC = 15
BDC = 27

def setup():
	GPIO.setmode(GPIO.BOARD)
	# Column switches
	GPIO.setup(SW1, GPIO.OUT)
	GPIO.setup(SW2, GPIO.OUT)
	GPIO.setup(SW3, GPIO.OUT)

	# Mux output select




if __name__ == "__main__":
	print("RPI RGB Matrix Test")
	setup()

	try:
		POST()
	except KeyboardInterrupt:
		print "Quit"
		GPIO.cleanup()
		

	GPIO.setup(R, GPIO.OUT)
	GPIO.setup(G, GPIO.OUT)
	GPIO.setup(B, GPIO.OUT)
	RPWM = GPIO.PWM(R, 100000)
	GPWM = GPIO.PWM(G, 100000)
	BPWM = GPIO.PWM(B, 100000)
	RPWM.start(colors[0][0])
	GPWM.start(colors[0][1])
	BPWM.start(colors[0][2])

	# Turn on all the LEDs
	GPIO.output(SW1, GPIO.HIGH)
	GPIO.output(SW2, GPIO.HIGH)
	GPIO.output(SW3, GPIO.HIGH)

	for j in range (500000000000): # this loop simply controls the "time" which the sim is active
		counter = 0
		for i in itertools.product([GPIO.LOW,GPIO.HIGH],repeat=3): # iterates over each LED
			GPIO.output(SW1, i[0])
			GPIO.output(SW2, i[1])
			GPIO.output(SW3, i[2])
#			print(i)
			time.sleep(1)
			# Change the colours
			RPWM.ChangeDutyCycle(colors[counter][0])
			GPWM.ChangeDutyCycle(colors[counter][1])
			BPWM.ChangeDutyCycle(colors[counter][2])
			#GPIO.output(R, colors[counter][0])
			#GPIO.output(G, colors[counter][1])
			#GPIO.output(B, colors[counter][2])
			counter +=1
	GPIO.cleanup()
	print("done")


