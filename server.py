#!/usr/bin/env python3

import socket
#use loopback address for ip if on same machine
#on server side- BLAR. on client side- connect.
import sys
import traceback
from threading import Thread


def server_program():
    host = "127.0.0.1"
    port = 1234 # non privileged port from 1024-65535
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print("Socket successfully created")
    try:
      server_socket.bind((host, port))
    except:
      print("Bind failed. Error : " + str(sys.exc_info()))
      sys.exit()


    server_socket.listen(5) #max. no. of connections the socket will establish
    print("Server socket is now in listen state")

    while True:
        conn, addr = server_socket.accept()
        ip, port = str(addr[0]), str(addr[1])

        print("User with IP : " +  ip + " and port : " + port + " has joined the chat")
        try:
            Thread(target=client_thread, args=(conn, ip, port)).start()
        except:
            print("Thread did not start.")
            traceback.print_exc()
    server_socket.close()


def client_thread(conn, ip, port, buffer_size = 1024):
   flag = 1
   while flag:
        data = conn.recv(buffer_size)
        data_size = sys.getsizeof(data)
        if data_size > buffer_size:
            print("Input size is more than buffer size {}".format(data_size))
        result = data.decode("utf8")
        
        if result == "--quit--":
            print("Client is requesting to quit")
            conn.close()
            print("User with IP : " + ip + " and port : " + port + " has left the chat")
            flag = 0
        else:
            print("User" + ip + ":" + port + " --> {}".format(result))
            conn.sendall("-".encode("utf8"))

if __name__ == "__main__":
   server_program()