import socket

HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
print(s)
print('server is ready')
conn, addr = s.accept()
print('connect by', addr, conn)
while 1:
    data = conn.recv(12)
    if not data:
        break
    conn.send(data)
conn.close()
