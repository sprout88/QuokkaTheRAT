# quokkaoTALK_server_infinite.py

import socket
import os

def send_message(sock):
    while True:
        message = input("Enter message: ")
        if message:
            break
        else:
            print("Input cannot be empty...")
    sock.send(message.encode('utf-8'))
    
    print("waiting for client...")

def receive_message(sock):
    try:
        data = sock.recv(1024).decode('utf-8',errors='ignore')
    except Exception as e:
        print(f'decode error : {e}')
    print("Received:", data)

# Set up the server socket
HOST = 'localhost'  # Use your server's IP address or hostname
PORT = 5000  # Use a free port number
try:
    server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(1)  # Listen for incoming connections
except Exception as e:
    print(f"연결 에러 발생 : {e}")
    os.system('pause')

print("quokkaoTALK Server started. Waiting for a client to connect...")

# Accept a client connection
client_socket, client_address = server_socket.accept()
print("Connected to client:", client_address)

while True:
    try:
        # Handle the client's messages
        receive_message(client_socket)
        send_message(client_socket)
    except Exception as e:
        print("클라이언트 연결이 끊어졌습니다...")
        os.system('pause')

        
