# @ Name: Prabir Tarafdar
# @ Date: 25/05/2021
import socket
HOST = 'localhost'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(5)
# print s
print('server is ready')
conn, addr = s.accept()
print('connect by', addr)
while True:
    data = conn.recv(1024).decode()
    tokens = data.split('#', 3)
    a = int(tokens[0])
    b = int(tokens[1])
    op = tokens[2]

    if op == '1':
        ans = a+b
    elif op == '2':
        ans = a-b
    elif op == '3':
        ans = a*b
    elif op == '4':
        if b != 0:
            ans = a/b
        else:
            conn.send(("Divisor should  not be 0").encode())
    conn.send(str(ans).encode())
    conn.close()
    break
s.close()
