import socket
HOST = 'localhost'
PORT = 5008
s = socket.socket()
s.bind(('', PORT))
s.listen(2)
# print(s)
print('FTP Server is ready....!!!')
print('you can Download a file.')
print("please be carefull writing filename, it is case sensetive..")
print("===============================================================")
conn, addr = s.accept()
print('connect by', addr, conn)
print('processing please wait.....')

while (1):

    f = open("Neel-Digante.mp3", "rb")
    l = f.read(1024)
    while(l):
        conn.send(l)
        l = f.read(1024)
        if len(l) == 0:
            break
        print('file sent successfully..')
    f.close()
    print('FTP Server: bye..')
    break
conn.close()
s.close()
