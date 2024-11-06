import RPi.GPIO as GPIO
import time

switchPin = 16
aPin = 12
bPin = 13
cPin = 14
dPin = 15
ePin = 17
fPin = 18
gPin = 19

pinList = [aPin, bPin, cPin, dPin, ePin, fPin, gPin]


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(switchPin, GPIO.IN)
for i in pinList:
    GPIO.setup(i, GPIO.OUT) 

# counts down from 9->0 when switch is pushed
def countdown():
    # Displaying 9
    GPIO.output(aPin, True)
    GPIO.output(fPin, True)
    GPIO.output(gPin, True)
    GPIO.output(bPin, True)
    GPIO.output(cPin, True)
    GPIO.output(dPin, True)
    GPIO.output(ePin, False)

    time.sleep(1)

    # Displaying 8
    GPIO.output(ePin, True)

    time.sleep(1)

    # Displaying 7
    GPIO.output(fPin, True)
    GPIO.output(gPin, True)
    GPIO.output(ePin, True)
    GPIO.output(dPin, True)

    # Displaying 6
    


while True:
    if(GPIO.input(switchPin)):
        countdown()
    else:
        for i in pinList:
            GPIO.output(i,False)
       


    
    