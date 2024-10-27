import RPi.GPIO as GPIO
import time
import numpy as np

# Set up GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# Define GPIO pins
button_pin = 36

# Set up button and LEDs
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

pins = np.array([8, 10, 12, 16, 18, 22, 24, 32, 26])
pins_list = (8, 10, 12, 16, 18, 22, 24, 32, 26)
GPIO.setup(pins_list, GPIO.OUT)
# Initialize state variables
blinking = False

def button_callback(channel):
    global blinking
    blinking = not blinking

# Set up event detection for the button
GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_callback, bouncetime=300)

try:
    while True:
        if blinking:
            for i in range(9):
                GPIO.output(int(pins[i]), True)
                time.sleep(0.1)
                GPIO.output(int(pins[i]), False)
        else:
            GPIO.output(pins_list, GPIO.LOW)

except KeyboardInterrupt:
    print("\nExiting program.")

finally:
    GPIO.cleanup()
