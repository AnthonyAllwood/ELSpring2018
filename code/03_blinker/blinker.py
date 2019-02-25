#!/usr/bin/python

#Import libraries
import RPi.GPIO as GPIO
import time

#Initialize the GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)

#This function makes the light blink once
def Blink():
	for i in range(0,17):
		print("blink#" +str(i+1))
		GPIO.output(17,True)
		time.sleep(1)
		GPIO.output(17,False)
		time.sleep(1)
	print("All finshed!!")

	GPIO.cleanup()

Blink()


