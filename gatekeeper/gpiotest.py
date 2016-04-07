import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def doorOpen(channel):
    print("Door Opened!")
    GPIO.wait_for_edge(23, GPIO.FALLING)
    print("Door Closed!")

print("Note how the bouncetime affects the button press")
GPIO.add_event_detect(23, GPIO.RISING, callback=doorOpen, bouncetime=1000)

while True:
    pass
