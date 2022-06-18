#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 5008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

a = input('Enter the First No.')
b = input('Enter the Second No.')
c = a+'/'+b
s.send(bytes(c, 'utf-8'))
data = s.recv(1024)
print('result = ', data)
