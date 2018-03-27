#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from socket import *      # Import necessary modules

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'home']

top = Tk()   # Create a top window
top.title('Sunfounder Raspberry Pi Smart Video Car')

HOST = '192.168.0.147'    # Server(Raspberry Pi) IP address
PORT = 21567
BUFSIZ = 1024             # buffer size
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)   # Create a socket
tcpCliSock.connect(ADDR)                    # Connect with the server

def forward_fun(event):
	print ('forward')
	tcpCliSock.send('forward'.encode())

def backward_fun(event):
	print ('backward')
	tcpCliSock.send('backward'.encode())

def left_fun(event):
	print ('left')
	tcpCliSock.send('left'.encode())

def right_fun(event):
	print ('right')
	tcpCliSock.send('right'.encode())

def stop_fun(event):
	print ('stop')
	tcpCliSock.send('stop'.encode())

def home_fun(event):
	print ('home')
	tcpCliSock.send('home'.encode())

def quit_fun(event):
	top.quit()
	tcpCliSock.send('stop')
	tcpCliSock.close()

def main():
	top.mainloop()

if __name__ == '__main__':
	main()
