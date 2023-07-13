# quokkaoTALK_client.py

import socket

def send_message(sock):
    message = input("Enter message: ")
    sock.send(message.encode('utf-8'))
    print("waiting for server...")

def receive_message(sock):
    data = sock.recv(1024).decode('utf-8')
    print("Received:", data)

# Set up the client socket
HOST = 'localhost'  # Use the server's IP address or hostname
PORT = 5000  # Use the same port number as the server

print("quokkaoTALK client start...")

# 연결을 요청한다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

# Start sending and receiving messages
print("Connected to the server. Start sending messages.")


send_message(client_socket)
receive_message(client_socket)

send_message(client_socket)
receive_message(client_socket)

send_message(client_socket)
receive_message(client_socket)

print("end quokkaoTALK client...")