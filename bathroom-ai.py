import RPi.GPIO as GPIO #import the GPIO library
import time
import requests
import json

BASE_URL = "https://bathroom-ai.herokuapp.com/api/rooms"
CHANGE_URL = BASE_URL + "/%s/%s"
FEMALE = 8
MALE = 10

ROOM_F_ID = 2
ROOM_M_ID = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(FEMALE, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(MALE, GPIO.IN, pull_up_down=GPIO.PUD_UP)

response = requests.get(BASE_URL)
result = dict(zip([x['id'] for x in r.json()], [x['occupied'] for x in r.json()]))

femaleDoorOccupied = result[ROOM_F_ID]
maleDoorOccupied = result[ROOM_M_ID]

def change_room_status(id, action):
     requests.post(CHANGE_URL % (id, action))

def free(id):
    change_room_status(id, FREE_ACTION)

def occupy(id):
    change_room_status(id, OCCUPY_ACTION)

while True:
    if GPIO.input(FEMALE):
        print("Door 1 is open")
        if femaleDoorOccupied:
            femaleDoorOccupied = False
            free(ROOM_F_ID)
        time.sleep(2)
    if GPIO.input(FEMALE) == False:
        print("Door 1 is closed")
        if not femaleDoorOccupied:
            femaleDoorOccupied = True
            occupy(ROOM_F_ID)
        time.sleep(2)
    if GPIO.input(MALE):
        print("Door 2 is open")
        if maleDoorOccupied:
            maleDoorOccupied = False
            free(ROOM_M_ID)
        time.sleep(2)
    if GPIO.input(MALE) == False:
        print("Door 2 is closed")
        if not maleDoorOccupied:
            maleDoorOccupied = True
            occupy(ROOM_M_ID)
        time.sleep(2)



