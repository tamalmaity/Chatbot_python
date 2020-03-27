import socket 

#only client can close connection in this using keyword : bye 
#use loopback address for ip if on same machine

def client_program():
	client_socket  = socket.socket()

	port = 12345
	host = raw_input ("Please enter client ip : ")

	client_socket.connect((host, port))

	while True:
		message = raw_input ("ENTER MESSAGE TO SEND TO SERVER: ")
		client_socket.send(message.encode()) 

		if message.lower().strip() == 'bye':
			break

		data = client_socket.recv(1024).decode()
		print ("Message received from server : " + data)

	client_socket.close()


if __name__ == '__main__':
	client_program()