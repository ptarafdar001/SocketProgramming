import socket
HOST = 'localhost'
PORT = 6008
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(bytes('200-100-50', 'utf-8'))
data = s.recv(1024)
print("200 - 100 - 50 = ", int(data))
