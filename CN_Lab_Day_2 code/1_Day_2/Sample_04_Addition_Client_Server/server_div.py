import socket
HOST = 'localhost'
PORT = 6666
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(3)
# print s
print('server is ready')
conn, addr = s.accept()
print('connect by', addr, conn)
while 1:
    data = conn.recv(1024)

    a, b = str(bytes(data), 'utf-8').split('/', 3)

    ans = int(a) / int(b)

    conn.send(bytes(str(ans), 'utf-8'))
    conn.close()
    break
s.close()
