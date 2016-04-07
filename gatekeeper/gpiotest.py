import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
   GPIO.wait_for_edge(23, GPIO.RISING)
   print("Cage Door is Open")
   GPIO.wait_for_edge(23, GPIO.FALLING)
   print("Cage Door is Closed")
