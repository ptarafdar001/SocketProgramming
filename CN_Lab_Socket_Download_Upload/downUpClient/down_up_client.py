import socket
import os

HOST = '192.168.0.7'
PORT = 5008
s = socket.socket()

s.connect((HOST, PORT))

fileList = os.listdir()

print("Enter your choice")
t = input("1. Downloade\n2. Uploade\n")
s.send(t.encode())

if t == '1':
    serverFile = s.recv(1024).decode()

    print("\n Files Available in Server:\n")
    print(serverFile)

    file = input(
        '\n Enter the file Name whice you want to downloade (ex: abc.mp3)\n')
    s.send(file.encode())

    print('downloading.....')
    f = open(file, "wb")
    l = s.recv(1024)
    size = 0
    while(l):
        f.write(l)
        size += len(l)
        l = s.recv(1024)
        if l == '':
            break
    print(f'file size={ size/1024} KB  \n downloaded successfully...')
    f.close()
    s.close()

elif t == "2":
    print("Available Files...")
    for i in range(len(fileList)):
        if i > 0:
            print(fileList[i])

    infile = input(
        '\n Enter the file Name whice you want to Uploade (ex: abc.mp3)\n')

    s.send(infile.encode())

    if(infile in fileList):
        print('uploading.....')
        f = open(infile, "rb")
        l = f.read(1024)
        while(l):
            s.send(l)
            l = f.read(1024)
            if len(l) == 0:
                break
        print(f'{infile} successfully Uploaded')
        f.close()
        s.close()
    else:
        print(f"{infile} not present in your device!!")
        s.close()
else:
    print("Enter valid Option!!!")
    s.close()
