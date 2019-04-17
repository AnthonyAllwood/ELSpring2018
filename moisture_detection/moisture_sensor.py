#!/usr/bin/python

#Import necessary libraries

import RPi.GPIO as GPIO
import time
import datetime
import os
import sqlite3  #This library will be used to log the timestamp and moisture readings to the database
import smtplib  #This is the library that will be utilized in order to send email notification
from gpiozero import MCP3008 #This library will be used for the MCP3008 ADC

import spidev #Used to communicate with SPI devices
from numpy import interp #Used in order to scale values

#Assign GPIO pin

sensorPin = 27

#Initialize the GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)

#Variable definitions

oldVal = 0

thresholdValue = 50

smtpUser = 'a.allwood9@gmail.com' #SMTO provider username
smtpPass = 'TB2freshh23' #SMTP provider password
emailSender = 'allwooda1@allwoodpi'
emailReceiver = 'a.allwood9@gmail.com'

#Message strings

no_moisture = """ From: Anthony Pi <allwoodpi>
To: Anthony Allwood <a.allwood9@gmail.com>
Subject: Moisure Sensor Message !!!

NO MOISTURE DETECTED ! """

moisture_detected = """ From: Anthony Pi <allwoodpi>
To: Anthony Allwood <a.allwood9@gmail.com>
Subject: Moisture Sensor message !!!

MOISTURE DETECTED ! """

moisture_low = """ From: Anthony Pi <allwoodpi>
To: Anthony Allwood <a.allwood9@gmail.com>
Subject: Moisture Level Update !!!

Moisture Content LOW! Plant is dry! Needs water! """

moisture_stable = """ From: Anthony Pi <allwoodpi>
To: Anthony Allwood <a.allwood9@gmail.com>
Subject: Moisture Level Update !!!

Moisture Content Stabilized! Plant watered! All good! """


#Function to send email
def sendEmail(message_send):
	try:
		smtpObject = smtplib.SMTP('smtp.gmail.com', 587)
		smtpObject.ehlo()
		smtpObject.starttls()
		smtpObject.ehlo()

		smtpObject.login(smtpUser, smtpPass)
		smtpObject.sendmail(emailSender, emailReceiver, message_send)

		smtpObject.quit()

		print "Email Successfully Sent!"

	except  smtplib.SMTPException:

		print "Error: Email was unable to send..."

#Function to determine if sensor is on or off
def isSensorOn(sensorPin):
	if GPIO.input(sensorPin):
		print "MOISTURE DETECTION OFF"
		sendEmail(no_moisture)

	else:
		print "MOISTURE DETECTION ON"
		sendEmail(moisture_detected)

#Function reads the moisture content value and sends an email notifying if moisture content is low or stable
def readContent(channel_0):
	spi = spidev.SpiDev()
	spi.open(0,0) #SPI port

	spi.max_speed_hz = 1350000
	adc = spi.xfer2([1,(8 + channel_0)<<4,0])
	raw_adc = ((adc[1]&3) << 8) + adc[2]

	moisture_Perc= interp(raw_adc, [0, 1023], [100, 0])
	moisture_Perc= int(moisture_Perc)

	print 'Moisture Content: ' , moisture_Perc,  '%'

	if moisture_Perc < thresholdValue:
		sendEmail(moisture_low)

	else:
		sendEmail(moisture_stable)

	return moisture_Perc

#Setup SQLite

db = sqlite3.connect("./log/moistureLog.db") #Creates databse in RAM
cursor = db.cursor() #Get cursor
db.commit() #Commit the changes above


try:
	while True:

		isSensorOn(sensorPin)
		readContent(0)

		time.sleep(30)

		content = readContent(0)

		#This sets the status variable depending on condition below
		if content < thresholdValue:
			status = "Plant not watered!"

		else:
			status ="Plant watered!"

		#If content value increases, it takes the exact time of when it increased (in unix time) and puts it in a text file.
		#This basically records when the plant was watered.
		if content > oldVal:
			cTime = time.time()
			wTime = time.time()
			os.system('echo '+str(wTime)+'>wateredTime.txt')
			wTime = os.popen('cat wateredTime.txt').read()
			oldVal = content

		else: #If it does not increase
			print "Moisture Content has not increased"

		elapsed_Unix = cTime - float(wTime) #Time elapsed from the last time plant was watered (unix time)

		elapsed = str(datetime.timedelta(seconds=elapsed_Unix)) #Time elapsed in days-hours-minutes-seconds. Sent to email.


		moisture_Content = '{0} %'.format(content)

		#Update timeStamp
		timeStamp = (time.strftime("%Y-%m-%d %H:%M:%S"))
		#Insert into moistureFormat table within database
		cursor.execute('''INSERT INTO moistureFormat VALUES(?,?,?)''', (timeStamp, str(moisture_Content), status))
		db.commit()
		all_rows = cursor.execute('''SELECT * FROM moistureFormat''')
		os.system('clear')
		for row in all_rows:
			print('{0} : {1} : {2}'.format(row[0], row[1], row[2]))

		#END

except KeyboardInterrupt:
	os.system('clear')
	print('Moisture Detection Complete!')
	GPIO.cleanup()

