# @ Name: Prabir Tarafdar
# @ Date: 25/05/2021
def menuBar():
    Dict = {
        1: 'Addition',
        2: 'Substraction',
        3: 'Multiplication',
        4: 'Division'
    }
    for i in Dict:
        print(f"{i} : {Dict.get(i)}")
    k = input("Enter Your Choice : ")
    return k


if __name__ == "__main__":

    import socket

    HOST = 'localhost'
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    op = menuBar()
    a = input('Enter the First No : ')
    b = input('Enter the Second No : ')

    c = a+'#'+b+'#'+op
    s.send(c.encode('ascii',))
    data = s.recv(1024)
    print('Result = ', data.decode())
    s.close()
