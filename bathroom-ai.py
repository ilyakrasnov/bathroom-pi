import RPi.GPIO as GPIO #import the GPIO library
import time
import urllib
import json

URL = 'http://bathroom-ai.herokuapp.com/api/rooms'
FEMALE = 8
MALE = 10

ROOM_F_ID = 2
ROOM_M_ID = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FEMALE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MALE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

response = json.loads(urllib.urlopen(URL).read())
result = dict(zip([x['id'] for x in response], [x['occupied'] for x in response]))

femaleDoorOccupied = result[ROOM_F_ID]
maleDoorOccupied = result[ROOM_M_ID]

def free_room(id):
    urllib.urlopen(URL + '/' + str(id) + '/free').read()
    

def occupy_room(id):
    urllib.urlopen(URL + '/' + str(id) + '/occupy').read()

while True:
    if GPIO.input(FEMALE):
        print("Door 1 is open")
        if femaleDoorOccupied:
            femaleDoorOccupied = False
            free_room(ROOM_F_ID)
        time.sleep(2)
    if GPIO.input(FEMALE) == False:
        print("Door 1 is closed")
        if not femaleDoorOccupied:
            femaleDoorOccupied = True
            occupy_room(ROOM_F_ID)  
        time.sleep(2)
    if GPIO.input(MALE):
        print("Door 2 is open")
        if maleDoorOccupied:
            maleDoorOccupied = False
            free_room(ROOM_M_ID)
        time.sleep(2)
    if GPIO.input(MALE) == False:
        print("Door 2 is closed")
        if not maleDoorOccupied:
            maleDoorOccupied = True
            occupy_room(ROOM_M_ID)  
        time.sleep(2)



