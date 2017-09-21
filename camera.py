from picamera import PiCamera
from time import sleep

camera = PiCamera()

#take a picture
camera.start_preview()
sleep(10)
camera.stop_preview()


#click and save it on desktop
camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/image.jpg')
camera.stop_preview()

#click 5 pictures
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/Desktop/test%s.jpg' % i)
camera.stop_preview()

#record a video for 10 sec and save it on desktop
camera.start_preview()
camera.start_recording('/home/pi/video.h264')
sleep(10)
camera.stop_recording()
camera.stop_preview()

#to run, open terminal and type omxplayer filename