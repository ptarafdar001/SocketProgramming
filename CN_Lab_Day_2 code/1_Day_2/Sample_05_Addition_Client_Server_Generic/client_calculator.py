def menuBar():
    Dict = {
        1: 'Addition',
        2: 'Substraction',
        3: 'Multiplication',
        4: 'Division'
    }
    for i in Dict:
        print(f"{i} : {Dict.get(i)}")
    k = int(input("Enter Your Choice : "))
    return k


if __name__ == "__main__":

    import socket

    HOST = 'localhost'
    PORT = 5000
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    val = menuBar()
    a = input('Enter the First No.')
    b = input('Enter the Second No.')

    if(val > 0 and val < 5):
        if val == 1:
            c = a+'+'+b
            s.send(c.encode('ascii',))
            data = s.recv(1024)
            print('result = ', data)
            s.close()
        if val == 2:
            c = a+'-'+b
            s.send(c.encode('ascii',))
            data = s.recv(1024)
            print('result = ', data)
            s.close()
        if val == 3:
            c = a+'*'+b
            s.send(c.encode('ascii',))
            data = s.recv(1024)
            print('result = ', data)
            s.close()
        if val == 4:
            c = a+'#'+b
            s.send(c.encode('ascii',))
            data = s.recv(1024)
            print('result = ', data)
            s.close()
    else:
        s.close()
