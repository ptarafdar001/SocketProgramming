import socket
from threading import Thread
#from SocketServer import ThreadingMixIn

TCP_IP = '192.168.0.7'
TCP_PORT = 8888
BUFFER_SIZE = 1024


class ClientThread(Thread):

    def __init__(self, ip, port, sock):
        Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.sock = sock
        print(" New thread started for "+ip+":"+str(port))

    def run(self):
        filename = 'Nill Digonte.mp3'
        f = open(filename, 'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.sock.send(l)

                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.sock.close()
                break


tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind((TCP_IP, TCP_PORT))
threads = []

while True:
    tcpsock.listen(5)
    print("Waiting for incoming connections...")
    (conn, (ip, port)) = tcpsock.accept()
    print('Got connection from ', (ip, port), conn)
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
