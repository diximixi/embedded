# Junghans controller

import board
from digitalio import DigitalInOut, Direction, Pull
from analogio import AnalogOut, AnalogIn
import touchio
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
import adafruit_dotstar as dotstar
import time
import neopixel

def volts(v):
    dacMax = (1<<16)-1
    vMax = 3.3
    return max(0, min(dacMax, int(v*dacMax/vMax)))

# Analog output on D0
analog_out = AnalogOut(board.A0)

######################### MAIN LOOP ##############################

while True:
    # Count up from 0 to 65535, with 64 increment
    # which ends up corresponding to the DAC's 10-bit range
    #for i in range(0, 65535, 64):
    #    analog_out.value = i
    #    time.sleep(0.01)
    analog_out.value = volts(3.3)
    time.sleep(0.5)
    analog_out.value = volts(0.0)
    time.sleep(0.5)