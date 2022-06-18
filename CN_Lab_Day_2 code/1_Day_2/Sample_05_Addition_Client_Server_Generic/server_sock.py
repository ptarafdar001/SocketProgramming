#!/usr/bin/env python
import socket

HOST = 'localhost'
PORT = 5008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)
# print s
print('server is ready')
conn, addr = s.accept()
print('connect by', addr, conn)
while 1:
    data = conn.recv(1024)

    a, b = str(bytes(data), 'utf-8').split('/')
    c = int(a) / int(b)
    conn.send(bytes(str(c), 'utf-8'))
    conn.close()
    break
s.close()
