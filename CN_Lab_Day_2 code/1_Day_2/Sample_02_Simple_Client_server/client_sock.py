import socket

HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
s.send(b'Hello, World')
data = s.recv(12)
s.close()
# print 'Received', repr(data)
print('Received-', data.decode())
