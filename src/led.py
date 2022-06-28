#!/bin/python3
import platform
if (platform.machine()=="ARM7"):

    #import RPi.GPIO as GPIO
    import time


    ledPin = 17

    #GPIO.setmode((GPIO.BOARD))



else:
    print("NOT proper type of platform!!!")