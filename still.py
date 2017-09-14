#!/usr/bin/python

from picamera import PiCamera
from time import sleep, strftime

timestamp = strftime("%Y-%m-%d_%H-%M-%S")
filename = '/home/pi/Desktop/cam_%s.jpg' % timestamp
camera = PiCamera()

camera.start_preview()
sleep(5)
camera.capture(filename)
camera.stop_preview()
