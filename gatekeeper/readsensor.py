import RPi.GPIO as GPIO
import sys
import json

GPIO.setmode(GPIO.BCM)

sensor_map_file = sys.argv[1]

try:
  sensor_map = json.load(open(sensor_map_file))
except Exception, e:
  print "\nFAILED! JSON error in file %s" % sensor_map_file
  print " Details: %s" % str(e)
  sys.exit(1)

print sensor_map

GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

while True:
   GPIO.wait_for_edge(23, GPIO.RISING, bouncetime=500)
   print("Cage Door is Closed")
   print GPIO.input(23)
   GPIO.wait_for_edge(23, GPIO.FALLING, bouncetime=500)
   print("Cage Door is Open")
   print GPIO.input(23)
