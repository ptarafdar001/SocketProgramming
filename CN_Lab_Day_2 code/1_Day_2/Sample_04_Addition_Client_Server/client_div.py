import socket

HOST = 'localhost'
PORT = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send('48/12'.encode())
data = s.recv(1024)
print("48 / 12 = ", data.decode())
