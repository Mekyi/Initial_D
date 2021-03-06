import Sunfounder_PWM_Servo_Driver.Servo_init as pwm
import RPi.GPIO as GPIO
import time

Motor0_A = 11  # pin11
Motor0_B = 12  # pin12
Motor1_A = 13  # pin13
Motor1_B = 15  # pin15

pins = [Motor0_A, Motor0_B, Motor1_A, Motor1_B]

EN_M0    = 4  # servo driver IC CH4
EN_M1    = 5  # servo driver IC CH5

p = pwm.init()

GPIO.setmode(GPIO.BOARD)

def setup():
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        setSpeed(50)

def setSpeed(speed):
	speed *= 40
	print('speed is: ', speed)
	p.setPWM(EN_M0, 0, speed)
	p.setPWM(EN_M1, 0, speed)


def stop():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)

def test_forward():
    GPIO.output(Motor0_A, GPIO.LOW)
    GPIO.output(Motor0_B, GPIO.HIGH)
    GPIO.output(Motor1_A, GPIO.HIGH)
    GPIO.output(Motor1_B, GPIO.LOW)
    time.sleep(2)

def test_backward():
    GPIO.output(Motor0_A, GPIO.HIGH)
    GPIO.output(Motor0_B, GPIO.LOW)
    GPIO.output(Motor1_A, GPIO.LOW)
    GPIO.output(Motor1_B, GPIO.HIGH)
    time.sleep(2)

setup()
test_forward()
test_backward()
stop()
