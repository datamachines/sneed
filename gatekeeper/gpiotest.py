import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
while True:
   GPIO.wait_for_edge(23, GPIO.RISING, bouncetime=500)
   print("Cage Door is Closed")
   print GPIO.input(23)
   GPIO.wait_for_edge(23, GPIO.FALLING, bouncetime=500)
   print("Cage Door is Open")
   print GPIO.input(23)
