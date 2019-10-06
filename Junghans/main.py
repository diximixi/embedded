# Junghans controller

import board
from digitalio import DigitalInOut, Direction, Pull
import time

class Motor:
    def __init__(self):
        self.__outF = DigitalInOut(board.D0)
        self.__outB = DigitalInOut(board.D1)
        self.__outF.direction = Direction.OUTPUT
        self.__outF.value = False
        self.__outB.direction = Direction.OUTPUT
        self.__outB.value = False

    def forward(self):
        self.stop()
        self.__outF.value = True

    def backward(self):
        self.stop()
        self.__outB.value = True

    def stop(self):
        self.__outF.value = False
        self.__outB.value = False
        time.sleep(0.2)


bellmotor = Motor()

# Main loop
while True:
    t = 2
    bellmotor.forward()
    time.sleep(t)
    bellmotor.stop()
    time.sleep(2.0)
    bellmotor.backward()
    time.sleep(t)
    bellmotor.stop()
    time.sleep(2.0)