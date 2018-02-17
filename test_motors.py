import RPi.GPIO as GPIO
import time

Motor0_A = 11  # pin11
Motor0_B = 12  # pin12
Motor1_A = 13  # pin13
Motor1_B = 15  # pin15

pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]

GPIO.setmode(GPIO.BOARD)

def setup():
    for pin in pins:
        GPIO.setup(pin, OUT)

def stop():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def test_forward():
    GPIO.output(Motor0_A, GPIO.LOW)
    GPIO.output(Motor0_B, GPIO.HIGH)
    GPIO.output(Motor1_A, GPIO.HIGH)
    GPIO.output(Motor1_B, GPIO.LOW)
    time(2)

setup()
test_forward()
stop()
