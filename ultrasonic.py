#! /usr/bin/python
# File name   : Ultrasonic.py
# Description : Detection distance  
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : Code
# Date        : 2018/08/22
import RPi.GPIO as GPIO
import time

Tr = 11
Ec = 8

def checkdist():#Reading distance
	print('u-1')
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(Tr, GPIO.OUT,initial=GPIO.LOW)
	GPIO.setup(Ec, GPIO.IN)
	GPIO.output(Tr, GPIO.HIGH)
	time.sleep(0.000015)
	GPIO.output(Tr, GPIO.LOW)
	print('u-2')
	while not GPIO.input(Ec):
		pass
	t1 = time.time()
	while GPIO.input(Ec):
		pass
	t2 = time.time()
	print('u-6')
	print((t2-t1)*340/2*100)
	return (t2-t1)*340/2*100

try:
        pass

except KeyboardInterrupt:
	GPIO.cleanup()
