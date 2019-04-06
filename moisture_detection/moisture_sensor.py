#!/usr/bin/python

#Import necessary libraries

import RPi.GPIO as GPIO
import time
import os
import sqlite3  #This library will be used to log the timestamp and moisture readings to the database
import smtplib  #This is the library that will be utilized in order to send email notification

#Assign GPIO pin

sensorPin = 27

#Initialize the GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)

#Variable definitions

detectNum = 1

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


def isSensorOn(sensorPin):
	if GPIO.input(sensorPin):
		print "MOISTURE DETECTION OFF"
		sendEmail(no_moisture)

	else:
		print "MOISTURE DETECTION ON"
		sendEmail(moisture_detected)


try:

	while True:

			for i in range (detectNum):
				isSensorOn(sensorPin)

			time.sleep(30)

			#END

except KeyboardInterrupt:
	os.system('clear')
	print('Moisture Detection Complete!')
	GPIO.cleanup()

