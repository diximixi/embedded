# Junghans controller

import board
from digitalio import DigitalInOut, Direction, Pull
import time

class Motor:
    def __init__(self, downTime = 0.0):
        self.__outF = DigitalInOut(board.D0)
        self.__outB = DigitalInOut(board.D1)
        self.__outF.direction = Direction.OUTPUT
        self.__outF.value = False
        self.__outB.direction = Direction.OUTPUT
        self.__outB.value = False
        self.__downTime = downTime

    def forward(self):
        wasBackward = self.__outB.value
        if (wasBackward):
            self.stop()
            time.sleep(self.__downTime)
        self.__outF.value = True

    def backward(self):
        wasForward = self.__outF.value
        if (wasForward):
            self.stop()
            time.sleep(self.__downTime)
        self.__outB.value = True

    def stop(self):
        self.__outF.value = False
        self.__outB.value = False

bellmotor = Motor(0.4)

# Main loop
while True:
    t = 2
    bellmotor.forward()
    time.sleep(t)
    #bellmotor.stop()
    #time.sleep(2.0)
    bellmotor.backward()
    time.sleep(t)
    #bellmotor.stop()
    #time.sleep(2.0)