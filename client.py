import socket
import sys
def main():
   client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   host = "127.0.0.1"
   port = 1234
   try:
      client_socket.connect((host, port))
   except:
      print("Connection Error")
      sys.exit()

   print("Type 'quit' to exit")
   message = input(" -> ")
   while message != 'quit':
      client_socket.sendall(message.encode("utf8"))
      message = input(" -> ")
   client_socket.send(b'--quit--')

if __name__ == "__main__":
   main()