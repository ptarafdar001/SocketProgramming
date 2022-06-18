import socket

HOST = 'localhost'
PORT = 5008
s = socket.socket()
print('you can download a file.')
print("please be carefull writing filename, it is case sensetive..")
print("===============================================================")
s.connect((HOST, PORT))
print('downloading.....')
f = open("Neel-Digantedownlode.mp3", "wb")
l = s.recv(1024)
size = 0
while(l):
    f.write(l)
    size += len(l)
    print(
        f'file size= {size/(1024)} Kilobytes downloaded. still downloading.....')
    l = s.recv(1024)
    if l == '':
        break

print(f'file size={ size/1024} KB   downloaded successfully...')
f.close()
s.close()
