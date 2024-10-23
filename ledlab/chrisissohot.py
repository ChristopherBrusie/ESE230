import RPi.GPIO as GPIO
import time

pressed = False
counter = 0
current = time.time()

while(True):
    if(time.time() > current + .05):
        pressed = GPIO.input(16)
        if pressed != last_pressed and last_pressed == False:
            counter += 1
        last_pressed = pressed
        print(counter)
        current = time.time()


