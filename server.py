import RPi.GPIO as GPIO
import motor
import direction
from socket import *

TCP_IP = ''  # 10.0.0.184
TCP_PORT = 21567
BUFFER = 1024
ADDRESS = (TCP_IP, TCP_PORT)

commands = ['forward', 'backward', 'stop', 'left', 'right', 'home']

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(ADDRESS)
serverSocket.listen(3)

GPIO.setmode(GPIO.BOARD)

direction.setup()
motor.setup()
direction.home()

while True:
    print('Trying to connect...')
    clientSocket, address = serverSocket.accept()
    print('Client connected from', address)

    while True:
        data = 'stop'
        data = clientSocket.recv(1024).decode()

        if data == '':
            break
        elif data == 'forward':
            motor.forward()
        elif data == 'backward':
            motor.backward()
        elif data == 'stop':
            motor.stop()
        elif data == 'left':
            direction.turn_left()
        elif data == 'right':
            direction.turn_right()
        elif data == 'home':
            direction.home()
            print('home')

        else:
            print('Cannot recognize' + data)
        print(data)

serverSocket.close
