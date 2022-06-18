import socket
HOST = 'localhost'
PORT = 5009
s = socket.socket()
s.bind(('', PORT))
s.listen(2)
print('FTP Server is ready....!!!')
print('you can upload a file.')
print("===============================================================")
conn, addr = s.accept()
print('connect by', addr, conn)
f = open("up.mp3", "wb")
l = conn.recv(1024)
size = 0
while(l):
    f.write(l)
    size += len(l)
    print(
        f'file size= ,{size/(1024)},Kilobytes downloaded. still downloading.....')
    l = conn.recv(1024)
    if l == '':
        break

print(f'file size={size/1024} KB   downloaded successfully...')
f.close()
conn.close()
s.close()
