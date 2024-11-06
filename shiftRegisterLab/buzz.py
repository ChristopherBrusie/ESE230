import RPi.GPIO as GPIO
import time

switchPin = 16
ledPin = 12
buzzPin = 13

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(switchPin, GPIO.IN)
GPIO.setup(ledPin, GPIO.OUT)
GPIO.setup(buzzPin, GPIO.OUT)

while True:
    if(GPIO.input(switchPin)):
        GPIO.output(ledPin,True)
        GPIO.output(buzzPin,True)
        time.sleep(1)
    else:
        GPIO.output(ledPin,False)
        GPIO.output(buzzPin,False)
