import socket
HOST = '192.168.0.7'
PORT = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(20)
print("I am online..")

name = input("Enter your name: ")
name = "@"+name+">"
print("waiting...")
conn, addr = s.accept()

while 1:
    data = conn.recv(50)
    print("\t\t"+data.decode())
    print(" "+name+">>")
    string = input()
    msg = name+","+string
    conn.send(msg.encode())
    if data == "quit":
        break
    if string == "quit":
        break

s.close()

conn.close()
