import Sunfounder_PWM_Servo_Driver.Servo_init as servo
import time

CONFIG_PATH = 'config.txt'

def Map(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def setup():
	global leftPWM, rightPWM, homePWM, pwm
	leftPWM = 400
	homePWM = 450
	rightPWM = 500
	offset = 0
	try:
		for line in open(CONFIG_PATH):
			if line[0:8] == 'offset =':
				offset = int(line[9:-1])
	except:
		print('config error')
	leftPWM += offset
	homePWM += offset
	rightPWM += offset
	pwm = servo.init()         # Initialize the servo controller.

def turn_left():
	global leftPWM
	pwm.setPWM(0, 0, leftPWM)  # CH0

def turn_right():
	global rightPWM
	pwm.setPWM(0, 0, rightPWM)

def turn(angle):
	angle = Map(angle, 0, 255, leftPWM, rightPWM)
	pwm.setPWM(0, 0, angle)

def home():
	global homePWM
	pwm.setPWM(0, 0, homePWM)

def calibrate(x):
	pwm.setPWM(0, 0, 450+x)

def test():
	turn_left()
	time.sleep(1)
	home()
	time.sleep(1)
	turn_right()
	time.sleep(1)
	home()

if __name__ == '__main__':
	setup()
    test()
	home()
