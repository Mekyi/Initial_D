import RPi.GPIO as GPIO
import time

Motor0_A = 11  # pin11
Motor0_B = 12  # pin12
Motor1_A = 13  # pin13
Motor1_B = 15  # pin15

pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]

GPIO.setmode(GPIO.BOARD)

def test_forward():
    GPIO.output(Motor0_A, GPIO.LOW)
    GPIO.output(Motor0_B, GPIO.HIGH)
    GPIO.output(Motor1_A, GPIO.LOW)
    GPIO.output(Motor1_B, GPIO.HIGH)
    time(2)
    stop()

def stop():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

test_forward()
