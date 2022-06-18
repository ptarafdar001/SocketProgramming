import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 8000

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)
print('Server is ready')
while True:
    # establish a connection
    clientsocket, addr = serversocket.accept()

    print("Got a connection from - %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
    break
serversocket.close()
