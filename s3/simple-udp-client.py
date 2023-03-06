import socket
import sys

def main():
    if len(sys.argv) < 3:
        print("not enough args")
    else:
        HOST, PORT = sys.argv[1:]
        PORT = int(PORT)
        # print(HOST, PORT)
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
            data = input('Enter your message: \n')
            client_socket.sendto(data.encode('utf-8'), (HOST,PORT))
            message, address = client_socket.recvfrom(1024) # putem sa primim mai mult decat incape (mai usor pe TCP)
            print(message)

if __name__ == '__main__':
    main()
