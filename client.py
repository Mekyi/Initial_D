from socket import *

ctrl_cmd = ['forward', 'backward', 'left', 'right', 'stop', 'home']

HOST = '10.0.0.184'
PORT = 21567
BUFSIZ = 1024
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
