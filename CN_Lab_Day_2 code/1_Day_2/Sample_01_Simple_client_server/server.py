import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = '192.168.0.5'  # Get local machine name
port = 6000            # Reserve a port for your service.
s.bind((host, port))        # Bind to the port

s.listen(5)                 # Now wait for client connection.
print(s)
print('server is ready')
while True:
    c, addr = s.accept()     # Establish connection with client.
    print(c)
    print('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()                # Close the connection
    break
s.close()
