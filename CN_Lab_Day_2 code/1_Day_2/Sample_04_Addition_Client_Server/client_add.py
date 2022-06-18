import socket

HOST = 'localhost'
PORT = 5008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(bytes('20+12+10', 'utf-8'))
data = s.recv(1024)
print("Result = ", int(data))
