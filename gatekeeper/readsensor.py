#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import json
import yaml
import requests
from datetime import datetime
#import time

GPIO.setmode(GPIO.BCM)

configfile = sys.argv[1]
conf = yaml.safe_load(open(configfile))

print conf

payload = {
"text":conf['message'],
"channel":conf['channel'],
"icon_emoji":conf['icon_emoji'],
"username": conf['username']
}

sensor_map_file = conf['sensor_map_file']

try:
  sensor_map = json.load(open(sensor_map_file))
except Exception, e:
  print "\nFAILED! JSON error in file %s" % sensor_map_file
  print " Details: %s" % str(e)
  sys.exit(1)

def slack(message):
    payload['text'] = message
    r = requests.post(conf['webhookurl'], data = json.dumps(payload))
    print "slack sent", r.text

def motion_sensed(channel):
    print "motion!"
    for ms in sensor_map["motion sensors"]:
        pin = int(ms['pin'])
        if pin == channel:
            name = ms['name']
    message = "Motion sensor " + name + " triggered."
    print message
    slack(message)

def door_change(channel):
    print "door change"
    for door in sensor_map["door sensors"]:
        pin = int(door['pin'])
        if pin == channel:
            name = door['name']
    state = GPIO.input(channel)
    status = "open"
    if state == 1:
        status = "closed"
    message = "Door " + name + " is now " + status
    print message
    slack(message)

for door in sensor_map["door sensors"]:
    pin = int(door['pin'])
    name = door['name']
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.BOTH, callback=door_change, bouncetime=500)
    print "Setting pin", pin, "pull down for", name

for ms in sensor_map["motion sensors"]:
    pin = int(ms['pin'])
    name = ms['name']
    GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(pin, GPIO.RISING, callback=motion_sensed, bouncetime=100)
    print "Setting pin", pin, "pull down for motion sensor", name

while True:
   pass
