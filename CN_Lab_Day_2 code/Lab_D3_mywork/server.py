import socket
host = '192.168.0.7'
port = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
# print(s)
print('server is ready')

while True:
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print("Connected With", addr, name)
    c.send(bytes(f'Thank you for connecting {name}', 'utf-8'))
    c.close()
s.close()
