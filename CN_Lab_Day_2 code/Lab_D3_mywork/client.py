import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.0.7'
port = 9999
s.connect((host, port))
name = input("Enter your name: ")
s.send(bytes(name, 'utf-8'))
print(s.recv(1024).decode())
s.close()
