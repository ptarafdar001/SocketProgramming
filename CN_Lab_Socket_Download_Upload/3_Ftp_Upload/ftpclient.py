import socket

HOST = 'localhost'
PORT = 5009
s = socket.socket()
s.connect((HOST, PORT))
print('you can upload a file.')
print("===============================================================")
print('uploading.....')
f = open("Neel-Digante.mp3", "rb")
l = f.read(1024)
while(l):
    s.send(l)
    l = f.read(1024)
    if len(l) == 0:
        break
    print('file sent successfully..')
f.close()
print('Done..')
s.close()
