import socket

HOST = 'localhost'
PORT = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
# print s
print('server is ready')
conn, addr = s.accept()
print('connect by', addr)
while 1:
    data = str(bytes(conn.recv(1024)), 'utf-8')

    if data.find('+') == True:
        a, b = data.split('+')
        c = int(a) + int(b)
        conn.send(bytes(str(c), 'utf-8'))
        conn.close()
        break
    if data.find('-') == True:
        a, b = data.split('-')
        c = int(a) - int(b)
        conn.send(bytes(str(c), 'utf-8'))
        conn.close()
        break
    if data.find('*') == True:
        a, b = data.split('*')
        c = int(a) * int(b)
        conn.send(bytes(str(c), 'utf-8'))
        conn.close()
        break
    if data.find('#') == True:
        a, b = data.split('#')
        c = int(a) // int(b)
        conn.send(bytes(str(c), 'utf-8'))
        conn.close()
        break

s.close()
