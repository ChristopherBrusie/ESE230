"""
For this program we will display 0-9 and then A-H for .5 seconds each using the shift register

      a
     ____
    |    |
f   |    |  b
    |_g__|
    |    |
 e  |    | c
    |____|
     d

from registers: a = 1st output, b = 2nd output, etc.

"""

zero = "11111110"
one = "01100000"
two = "11011101"
three = "11111001"
four = "01111011"
five = "10111011"
six = "10111111"
seven = "11100000"
eight = "11111111"
nine = "11111011"
a = "11101111"
b = "00111111"
c = "10011110"
d = "01111101"
e = "10011111"
f = "10001111"
g = "11111011"
h = "01101111"

list = [zero, one, two, three, four, five, six, seven, eight, nine, a, b, c, d, e, f, g, h]

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
    time.sleep(.5)


for i in list:
    flipflop(i)
