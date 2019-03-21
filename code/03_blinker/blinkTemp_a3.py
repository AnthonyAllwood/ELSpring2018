#!/usr/bin/python

#Import libraries that will be utilized
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3
from flask import Flask, render_template
app = Flask(__name__)

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
blinkNum= 7
#--------------------------------------------------------------------
#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(redPin,GPIO.OUT)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#Setup SQLite
db = sqlite3.connect('./log/assignment3.db') #Creates database in RAM
cursor = db.cursor() #Get cursor
db.commit() #Commit the changes above^^



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

	with open("./log/assignment3.csv", "a") as log:

		while True:
			#input_state = GPIO.input(buttonPin)
			#if input_state == False:
			for i in range (blinkNum):
				oneBlink(redPin)

			time.sleep(60)
			data = readF(tempPin)
			#print (data)
			log.write("{0},{1}\n".format(time.strftime("%Y-%m-%d %H:%M:%S"),str(data)))
			timeNow = (time.strftime("%Y-%m-%d %H:%M:%S"))
			cursor.execute('''INSERT INTO tempFormat VALUES(?,?)''', (timeNow, str(data)))
			db.commit()
			all_rows = cursor.execute('''SELECT * FROM tempFormat''')
			for row in all_rows:
				print('{0} : {1}' .format(str(row[0]), row[1],))
			#END

except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
	db.close()

