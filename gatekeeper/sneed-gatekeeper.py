#!/usr/bin/python
import yaml
import requests
import json
import RPi.GPIO as GPIO
import datetime

configfile = "../../sneedconfig.yaml"
conf = yaml.safe_load(open(configfile))

print conf
payload = {
"text":conf['message'],
"channel":conf['channel'],
"icon_emoji":conf['icon_emoji'],
"username": conf['username']
}

def slack(message):
    payload['text'] = message
    r = requests.post(conf['webhookurl'], data = json.dumps(payload))
    print r.text

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
   GPIO.wait_for_edge(23, GPIO.RISING, bouncetime=500)
   time = datetime.now().isoformat()
   print("Cage Door is Closed " + time)
   slack("Cage Door is Closed")
   GPIO.wait_for_edge(23, GPIO.FALLING, bouncetime=500)
   time = datetime.now().isoformat()
   print("Cage Door is Open " + time)
   slack("Cage Door is Open")
