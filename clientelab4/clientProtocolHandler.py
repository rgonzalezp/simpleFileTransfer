import socket


BUFFER_SIZE = 1024


def handler(sock):

    # Receive the folders available
    folders = sock.recv(1024)
    print(folders)

    # First send to the server which folder to ask for
    message = input("Folder to ask for:")
    sock.sendall(bytes(message, 'ascii'))

    response = str(sock.recv(BUFFER_SIZE), 'ascii')

    print("Received: {}".format(response))

    file = input("File to ask for? (From The list): ")
    sock.sendall(bytes(file, 'ascii'))

    with open("repo/" + file, 'wb') as f:
        pck = sock.recv(BUFFER_SIZE)
        while pck:
            f.write(pck)
            pck = sock.recv(BUFFER_SIZE)


def client(ip, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((ip, port))
        handler(sock)
def main():
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 27000
    client(HOST, PORT)

if __name__ == "__main__":
    main()
