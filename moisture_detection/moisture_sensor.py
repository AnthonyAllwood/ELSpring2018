#!/usr/bin/python

#Import necessary libraries

import Rpi.GPIO as GPIO
import time
import os
import sqlite3  #This library will be used to log the timestamp and moisture readings to the database
import smtplib  #This is the library that will be utilized in order to send email notification

#Assign GPIO pin

sensorPin = 27
analogPin = 26
#Initialize the GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensorPin, GPIO.IN)
GPIO
#Variable definitions

detectNum = 3

user_smtp = "a.allwood9@gmail.com" #SMTO provider username
password_smtp = "TB2freshh23" #SMTP provider password
host_smtp = "allwooda1" #SMTP provider hostname
port_smtp = 25 #SMTP provider port
email_receiver = ['a.allwood9@gmail.com']

#Message strings

no_moisture = ''' From: Anthony Pi <allwoodpi>
To: Anthony Allwood <a.allwood9@gmail.com>
Subject: Moisure Sensor Message !!!

NO MOISTURE DETECTED ! '''

moisture_detected = ''' From: Anthony Pi <allwoodpi>
To: Anthony Allwood <a.allwood9@gmail.com>
Subject: Moisture Sensor message !!!

MOISTURE DETECTED ! '''

#Function to send email

def sendEmail(message_send):
	try:
		object_Smtp = stmplib.SMTP(host_smtp, port_smtp)
		object_Smtp.login(user_smtp, password_smtp)
		object_Smtp.sendmail(email_receiver, message_send)

		print "Email Successfully Sent!"

	except  smtplib.SMTPException:

		print "Error: Email was unable to send..."


def isSensorOn(sensorPin):
	if GPIO.input(sensorPin):
		print "MOISTURE DETECTION OFF"
		sendEmail(no_moisture)

	else:
		print "MOISTURE DETECTION ON"
		sendEmail(moisture_detection)


def readSensorH(analogPin)
