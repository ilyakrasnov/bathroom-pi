import RPi.GPIO as GPIO #import the GPIO library
import time
import urllib2
import json

URL = 'http://bathroom-ai.herokuapp.com/api/occupations'
FEMALE = 8
MALE = 10

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FEMALE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MALE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

response = json.loads(urllib2.urlopen(URL).read())
result = dict(zip([x['name'] for x in response], [x['occupied'] for x in response]))

femaleDoorOccupied = result['F']
maleDoorOccupied = result['M']

while True:
    if GPIO.input(FEMALE):
        print("Door 1 is open")
        femaleDoorOccupied = False
        time.sleep(2)
    if GPIO.input(FEMALE) == False:
        print("Door 1 is closed")
        femaleDoorOccupied = True
        time.sleep(2)
    if GPIO.input(MALE):
        print("Door 2 is open")
        maleDoorOccupied = False
        time.sleep(2)
    if GPIO.input(MALE) == False:
        print("Door 2 is closed")
        maleDoorOccupied = True
        time.sleep(2)



