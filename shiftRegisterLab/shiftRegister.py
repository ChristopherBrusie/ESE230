# For this program we need to turn on all the pins for 1 second and then turn them all off for 1 second

import RPi.GPIO as GPIO
import time

Data = 36 #GPIO 16
Clock = 22 #GPIO 25
Latch = 32 #GPIO 12


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(Data, GPIO.OUT)
GPIO.setup(Clock, GPIO.OUT)
GPIO.setup(Latch, GPIO.OUT)

GPIO.output(Latch, 0)
GPIO.output(Clock, 0)

# sequence must be 8 characters long
def flipflop(sequence):
    for n in range(8):
        GPIO.output(Data, int(sequence(n)))
        GPIO.output(Clock, 1) # Clock pulse set to 1 to shift serial data.
        GPIO.output(Clock, 0) # Clock pulse off.
        #end for statement.

    GPIO.output(Latch, 1) # Now the latch is set to high to allow parallel data output


Sequence_i = "11111111"
Sequence_ii = "00000000"

# Following sequence outlined in lab handout
flipflop(Sequence_i)
time.sleep(1)
flipflop(Sequence_ii)
time.sleep(1)
flipflop("10101010")
time.sleep(1)
flipflop("01010101")
time.sleep(1)
flipflop(Sequence_i)
time.sleep(1)
flipflop(Sequence_ii)


