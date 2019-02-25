#!/usr/bin/python

#Import libraries that will be utilized
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os

#Assign GPIO pins
redPin = 27
tempPin = 17
buttonPin = 26

#Temp Sensor and Humidity Sensor
tempSensor = Adafruit_DHT.DHT11

#-------------------------------------------------------------------
#LED variables
#Duration of Blinks
blinkDuration = 0.1

#number of times to Blink the LED
blinkNum= 8
#--------------------------------------------------------------------
#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def oneBlink(pin):
	GPIO.output(pin,True)
	time.sleep(blinkDuration)
	GPIO.output(pin,False)
	time.sleep(blinkDuration)

def readF(tempPin):
	humidity, temperature = Adafruit_DHT.read_retry(tempSensor, tempPin)
	temperature = temperature * 9/5.0 +32
	if humidity is not None and temperature is not None:
		tempFahr = '{0:0.1f}*F'.format(temperature)
	else:
		print('Cant Read Temp Sensor')
	return tempFahr

try:
	while True:
		input_state = GPIO.input(buttonPin)
		if input_state == False:
			for i in range (blinkNum):
				oneBlink(redPin)
			time.sleep(.2)
			data = readF(tempPin)
			print (data)

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
