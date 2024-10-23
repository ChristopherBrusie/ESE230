import RPi.GPIO as GPIO
import time
import numpy as np

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(8, GPIO.OUT)
GPIO.setup(10, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(32, GPIO.OUT)
GPIO.setup(36, GPIO.IN)

pins = (8, 10, 12, 16, 18, 22, 24, 26, 32)
pins_arr = np.array([8, 10, 12, 16, 18, 22, 24, 26, 32])

while True:
    if GPIO.input(36):
        for i in range(9):
            GPIO.output(int(pins_arr[i]), True)
            time.sleep(0.1)
            GPIO.output(int(pins_arr[i]), False)
    else:
        GPIO.output(pins, False);