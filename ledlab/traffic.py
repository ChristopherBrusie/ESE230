import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

start_time = time.time()
cur_time = start_time
while(True):
    GPIO.output(8,True)
    GPIO.output(10,True)
    time.sleep(3)
    GPIO.output(10,False)
    time.sleep(4)
    GPIO.output(8,False)
    GPIO.output(12,True)
    time.sleep(3)
    for i in range(6):
        on = True
        GPIO.output(12,on)
        on = not on
        time.sleep(0.25)
    GPIO.output(16,True)
    time.sleep(5)
    GPIO.output(16,False)
        


GPIO.cleanup()