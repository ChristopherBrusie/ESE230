import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(16, GPIO.IN)
GPIO.setup(12, GPIO.OUT)

while True:
    if(GPIO.input(16)):
        GPIO.output(12,True)
    else:
        GPIO.output(12,False)