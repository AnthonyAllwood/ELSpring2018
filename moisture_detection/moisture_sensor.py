#!/usr/bin/python

#Import necessary libraries

import RPi.GPIO as GPIO
import time
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

thresholdValue = 4.0

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

def readContent():
	voltageRead = MCP3008(0)

	actualVoltage = voltageRead.value * 10
	print(actualVoltage)

	if actualVoltage >= thresholdValue:
		print "Plant is dry! Needs water!"

	else:
		print "Plant watered! All good!"

def readContentTwo(channel_0):
	spi = spidev.SpiDev()
	spi.open(0,0) #SPI port

	spi.max_speed_hz = 1350000
	adc = spi.xfer2([1,(8 + channel_0)<<4,0])
	raw_adc = ((adc[1]&3) << 8) + adc[2]

	moisture_Perc= interp(raw_adc, [0, 1023], [100, 0])
	moisture_Perc= int(moisture_Perc)
	print 'Moisture Content: ' , moisture_Perc,  '%'

try:

	while True:

			for i in range (detectNum):
				#isSensorOn(sensorPin)
				readContentTwo(0)

			time.sleep(10)

			#END

except KeyboardInterrupt:
	os.system('clear')
	print('Moisture Detection Complete!')
	GPIO.cleanup()

