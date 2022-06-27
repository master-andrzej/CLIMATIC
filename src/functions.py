
import RPi.GPIO as GPIO

_DHT_pin = 26


def setInput():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(_DHT_pin, GPIO.IN)
    


def getTemp