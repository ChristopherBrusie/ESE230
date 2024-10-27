import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(36, GPIO.IN)
pressed = False
counter = 0
current = time.time()
last_pressed = True;

while(True):
    if(time.time() > current + .05):
        pressed = GPIO.input(36)
        if pressed != last_pressed and last_pressed == False:
            counter += 1
            print(counter)
        last_pressed = pressed
        current = time.time()


