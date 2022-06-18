import socket

HOST = '192.168.0.7'
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

name = input("Enter your name: ")
name = "@"+name+">"
print("now you can start your chat..")
while 1:
    print(name+">>")
    string = input()
    msg = name+","+string
    s.send(msg.encode())
    data = s.recv(50)
    print(data.decode())
    if data == "quit":
        break
    if string == "quit":
        break

s.close()
