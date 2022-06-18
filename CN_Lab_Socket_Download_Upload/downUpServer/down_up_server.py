import socket
import os
HOST = 'localhost'
PORT = 5008
s = socket.socket()
s.bind(('', PORT))
s.listen(2)
print('FTP Server is ready....!!!')
conn, addr = s.accept()
print('connect by', addr)
itemList = os.listdir()

x = conn.recv(1024).decode()

if x == "1":
    conn.send(str(itemList).encode())  # send present file list

    keyfile = conn.recv(1024).decode()  # receve the expected file name
    if(keyfile in itemList):
        while (1):
            f = open(keyfile, "rb")
            l = f.read(1024)
            while(l):
                conn.send(l)
                l = f.read(1024)
                if len(l) == 0:
                    break
            print(f'{keyfile} - sent successfully..')
            f.close()
            break
        conn.close()
        s.close()
    else:
        conn.send("Not".encode())
        conn.close()
        s.close()
if x == '2':
    recvFileName = conn.recv(1024)

    f = open(recvFileName, "wb")
    l = conn.recv(1024)
    size = 0
    while(l):
        f.write(l)
        size += len(l)
        l = conn.recv(1024)
        if l == '':
            break
    print(f'file size={size/1024} KB  \n Receved successfully...')

    f.close()
    conn.close()
    s.close()

else:
    conn.close()
    s.close()
