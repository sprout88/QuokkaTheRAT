# quokkaoTALK_client.py

import socket

def send_message(sock):
    message = input("Enter message: ")
    sock.send(message.encode('utf-8'))
    print("waiting for client...")

def receive_message(sock):
    data = sock.recv(1024).decode('utf-8')
    print("Received:", data)

# Set up the server socket
HOST = 'localhost'  # Use your server's IP address or hostname
PORT = 5000  # Use a free port number

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)  # Listen for incoming connections

print("Server started. Waiting for a client to connect...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

# Handle the client's messages
receive_message(client_socket)
send_message(client_socket)

receive_message(client_socket)
send_message(client_socket)

receive_message(client_socket)
send_message(client_socket)

# Clean up the client connection and close the server socket
client_socket.close()
server_socket.close()