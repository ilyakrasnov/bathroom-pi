import RPi.GPIO as GPIO #import the GPIO library
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_UP)

door_1_open = 0
door_2_open = 0

while True:
    if GPIO.input(8):
       print("Door 1 is open")
       time.sleep(2)
    if GPIO.input(8) == False:
       print("Door 1 is closed")
       time.sleep(2)
    if GPIO.input(10):
       print("Door 2 is open")
       time.sleep(2)
    if GPIO.input(10) == False:
       print("Door 2 is closed")
       time.sleep(2)


