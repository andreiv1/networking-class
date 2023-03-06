import socket

def main():
    HOST, PORT = 'localhost', 3334
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind(('',3334))

        while True:
            message, address = server.recvfrom(1024)
            server.sendto(message.upper(), address)
            print(f"Sent to {address}")

if __name__ == '__main__':
    main()