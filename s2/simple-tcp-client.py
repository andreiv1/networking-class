import socket

HOST, PORT = 'localhost', 3333

def main():
                                        # TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST,PORT))
        client.sendall(b'this is some text')
        data = client.recv(1024) # aceeasi lungime a buff si pe server si pe client
        print(data)

if __name__ == '__main__':
    main()