from gpiozero import MotionSensor
import pygame
from time import sleep
import pigpio
import RPi.GPIO as GPIO

pi = pigpio.pi()

pir = MotionSensor(23)

pygame.init()
pygame.mixer.init()

door = pygame.mixer.Sound("piano2.wav")
try:
    while True:
        pir.wait_for_motion()
        sleep(2)
        print("Motion detected!")
        pi.set_PWM_dutycycle(17, 255)
        pi.set_PWM_dutycycle(22, 255)
        pi.set_PWM_dutycycle(24, 255)
        for i in range(0, 2):
            door.play()
            sleep(7)
        pir.wait_for_no_motion()
        pi.set_PWM_dutycycle(17, 0)
        pi.set_PWM_dutycycle(22, 0)
        pi.set_PWM_dutycycle(24, 0)
except KeyboardInterrupt:
    pi.set_PWM_dutycycle(17, 0)
    pi.set_PWM_dutycycle(22, 0)
    pi.set_PWM_dutycycle(24, 0)
    GPIO.cleanup()
