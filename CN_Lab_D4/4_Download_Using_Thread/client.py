import socket

TCP_IP = '192.168.0.7'
TCP_PORT = 8888
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
size = 0
with open('Nill Digonte(download).mp3', 'wb') as f:
    print('file opened')
    while True:
        print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        #print('data=%s', (data))

        if not data:
            f.close()
            print('file close()')
            break
        # write data to a file
        f.write(data)

print('Successfully get the file')
s.close()
print('connection closed')
