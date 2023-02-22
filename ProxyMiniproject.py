import socket
import time

PORT = 5050

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_socket.bind(('127.0.0.1', PORT))

# Start listening for incoming connections
server_socket.listen()
print("proxy listening on 127.0.0.1", PORT)

# Accept incoming connections
while True:
  client_socket, client_addr = server_socket.accept()
  print("Client connected to proxy on 127.0.0.1, port: ", PORT)

  # Receive data from the client
  data = client_socket.recv(4096)

  # Forward the data to the destination server
  destination_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  destination_server.connect(('127.0.0.1', 8080))
  destination_server.sendall(data)

  print("sending data to server at 127.0.0.1,", 8080)

  # Receive data from the destination server
  response = destination_server.recv(4096)
  print("proxy recieved response from the server!")  
  # Send the response back to the client
  client_socket.sendall(response)
  print("proxy sent data to client")