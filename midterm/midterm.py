#!/usr/bin/python

#Import Libraries we will be using
import RPi.GPIO as GPIO
import time
import os
import sqlite3
import sys

#Assign GPIO pins
entrySensor = 13
exitSensor = 26

#Stabilization time
stableTime = 5
#---------------------------------------------------------------------
#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(entrySensor, GPIO.IN)
GPIO.setup(exitSensor, GPIO.IN)

#SQLite setup
db = sqlite3.connect('./log/logPeople.db')
cursor = db.cursor() #Get cursor
db.commit() #Commit Changes

#Using Simon's code

def bothTriggers(trigger2, wait=5):
	timeStamp = False
	#This is the sanity check.  If the second sensor isn't triggered, it resets.
	#The sanity check only happens while the second sensor is in a low state (not triggered)
	timeCheck = time.time()
	while not GPIO.input(trigger2):
		if time.time() - timeCheck > wait:
        		break
       	        continue
		if time.time() - timeCheck <= wait:
        		timeStamp = time.strftime("%Y-%m-%d %H:%M:%S")
        		time.sleep(4)
        	continue

#Stabilize sensor
time.sleep(10)
#Initialize people in room
peopleCount = 0

try:
	while True:
		#Reset timeStamp to false to prevent writing data until both sensors are triggered again
		timeStamp = False
		#set entry Type
		inOrOut = "IDLE"

        	if GPIO.input(entrySensor):
			timeStamp = bothTriggers(exitSensor)
			if timeStamp:
				inOrOut = "Entrance"
				peopleCount = peopleCount + 1
		if GPIO.input(exitSensor):
			timeStamp = bothTriggers(entrySensor)
			if timeStamp:
				inOrOut = "Exit"
				peopleCount = peopleCount - 1

#Since the timeStamp is only set when the direction is determined and both sensors are triggered we use that as the condition to write our data:
		if timeStamp:
			cursor.execute('''INSERT INTO logPeople VALUES(?,?,?)''', (timeStamp, inOrOut, peopleCount))
			db.commit()
			all_rows = cursor.execute('''SELECT * FROM logPeople''')
			os.system('clear')
			for row in all_rows:
				print('{0} : {1} : {2}'.format(str(row[0]), row[1], str(row[2])))

except db.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

except KeyboardInterrupt:
        GPIO.cleanup()
        db.close()
        print('Motion was detected and recorded!!!')
