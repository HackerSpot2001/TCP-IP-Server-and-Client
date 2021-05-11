#!/usr/bin/python3
import socket
import threading

def handle_clients(client):
    client.send("Confirmation Message...".encode("utf-8"))

def recieve_connections():
    while True:
        try:
            client,addr = server.accept()
            print(f"[+] {addr} is connected with server")
            thread = threading.Thread(target=handle_clients,args=(client,))
            thread.start()
        
        except Exception as e:
            print("Error:- ",e)


host = "127.0.0.1"
port = 9090
# host = str(input("IP address: "))
# port = int(input("Port: "))
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((host,port))
print(f"[+] Server is running on {host}:{port}")
server.listen()
recieve_connections()