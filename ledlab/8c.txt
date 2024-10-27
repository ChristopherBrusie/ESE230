import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()
GPIO.setup(36, GPIO.IN)
pins_list = (8, 10, 12, 16, 18, 22, 24, 32, 26)
pins = np.array([8, 10, 12, 16, 18, 22, 24, 32, 26])
GPIO.setup(pins_list, GPIO.OUT)
pressed = False
counter = 1
current = time.time()
last_pressed = True;

while(True):
    if(time.time() > current + .05):
        pressed = GPIO.input(36)
        if pressed != last_pressed and last_pressed == False:
            counter += 1
            GPIO.output(pins_list[counter%len(pins_list)], True)
            GPIO.output(pins_list[(counter%len(pins_list)) -1], False)
        last_pressed = pressed
        current = time.time()


GPIO.cleanup()