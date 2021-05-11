#!/usr/bin/python3
import socket
import threading

host = "127.0.0.1"
port = 9090

try:
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    recv = client.recv(1024).decode('utf-8')
    print(recv)
    

except:
    pass