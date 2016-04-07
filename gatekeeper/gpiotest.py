import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

def doorOpen(channel):
    print("Door Opened!")

def doorClose(channel):
    print("Door Closed!")

print("Note how the bouncetime affects the button press")
GPIO.add_event_detect(23, GPIO.RISING, callback=doorOpen, bouncetime=1000)
GPIO.add_event_detect(23, GPIO.FALLING, callback=doorClosed, bouncetime=1000)
