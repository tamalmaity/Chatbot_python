import socket
#use loopback address for ip if on same machine

def server_program():
	server_socket = socket.socket()

	port = 12345
	host = raw_input ("Please enter client ip : ") # socket.gethostname()
	server_socket.bind(("host", port))
	print 'Bounded to port'

	server_socket.listen(2)   #max. no. of connections the socket will establish

	conn, addr = server_socket.accept()
	print 'connected to', addr

	while True:
		data = conn.recv(1024).decode()
		print ("Message received from client : " + data)

		if data.lower().strip() == 'bye':
			break

		message = raw_input ("ENTER MESSAGE TO SEND TO CLIENT: ")
		conn.send(message.encode())
		
	conn.close()


if __name__ == '__main__':
	server_program()