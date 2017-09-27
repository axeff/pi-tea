#!/usr/bin/python

import RPi.GPIO as GPIO
import time

# Use the pin numbers from the ribbon cable board. 
GPIO.setmode(GPIO.BCM) 
# Set up the pin you are using ("17" is an example) as output. 
GPIO.setup(17, GPIO.OUT) 

def getTemperature():
	# Open the file that we viewed earlier so that python can see what is in it. Replace the serial number as before. 
	tfile = open("/sys/bus/w1/devices/28-00000513f208/w1_slave")
	# Read all of the text in the file. 
	text = tfile.read()
	# Close the file now that the text has been read. 
	tfile.close()
	# Split the text with new lines (\n) and select the second line. 
	secondline = text.split("\n")[1]
	# Split the line into words, referring to the spaces, and select the 10th word (counting from 0). 
	temperaturedata = secondline.split(" ")[9]
	# The first two characters are "t=", so get rid of those and convert the temperature from a string to a number. 
	temperature = float(temperaturedata[2:])
	# Put the decimal point in the right place and display it. 
	temperature = temperature / 1000
	print temperature
	return temperature

while True:
	
	temperature = getTemperature()
	if temperature >= 29.0:
		# Turn on the pin and see the LED light up. 
		GPIO.output(17, GPIO.HIGH)
	else:
		#Turn off the pin to turn off the LED. 
		GPIO.output(17, GPIO.LOW)
	time.sleep(1)
