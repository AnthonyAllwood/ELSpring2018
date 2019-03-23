#!/usr/bin/python

#Import these libraries
import RPi.GPIO as GPIO
import time
import os
import sqlite3
import sys

#Assign GPIO pins 13 and 26
entrySensor = 13
exitSensor = 26

#Initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(entrySensor, GPIO.IN)
GPIO.setup(exitSensor, GPIO.IN)

#------------------------------------------------
#SQLite setup
db = sqlite3.connect('./log/logPeople.db')
cursor = db.cursor() #Get cursor
db.commit() #Commit Changes
#------------------------------------------------

def bothTriggers(trigger2, wait=5):
	timeStamp = False
	#In case second sensor is not triggered
	timeCheck = time.time()
	while not GPIO.input(trigger2):
		if time.time() - timeCheck > wait:
        		break
       	        continue
		if time.time() - timeCheck <= wait:
        		timeStamp = time.strftime("%Y-%m-%d %H:%M:%S")
        		time.sleep(4)
        	continue

#Sensor stabilization for 10 seconds
time.sleep(10)

#Keeps track of how many people are in the room
peopleCount = 0

try:
	while True:
		#This resets the timeStamp to false to prevent writing data until both sensors are triggered again
		timeStamp = False

		#This sets the entry Type
		inOrOut = "IDLE"

        	if GPIO.input(entrySensor):
			#This print line tests to see if entrySensor is functional
			print("entrySensor triggered")
			timeStamp = bothTriggers(exitSensor)
			if timeStamp:
				inOrOut = "Entrance"
				peopleCount = peopleCount + 1
		if GPIO.input(exitSensor):
			#This print line tests to see if exitSensor is functional
			print("exitSensor triggered")
			timeStamp = bothTriggers(entrySensor)
			if timeStamp:
				inOrOut = "Exit"
				peopleCount = peopleCount - 1

#Writes data to the logPeople table in the database:
		if timeStamp:
			cursor.execute('''INSERT INTO logPeople VALUES(?,?,?)''', (timeStamp, inOrOut, peopleCount))
			db.commit()
			all_rows = cursor.execute('''SELECT * FROM logPeople''')
			os.system('clear')
			for row in all_rows:
				print('{0} : {1} : {2}'.format(str(row[0]), row[1], str(row[2])))

	time.sleep(10)

except db.Error, e:
	print "Error %s:" %e.args[0]
	sys.exit(1)

except KeyboardInterrupt:
        GPIO.cleanup()
        db.close()
        print('Motion was detected and recorded!!!')
