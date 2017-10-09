import socketserver
import os


BUFFER_SIZE = 1024


def getFiles(dir):
    return os.listdir("./files/" + dir)


class Handler(socketserver.BaseRequestHandler):

    def setup(self):

        self.request.settimeout(120)

    def handle(self):

        # Send the avaiable folders
        folders = " ".join(getFiles(""))
        self.request.sendall(bytes(folders, 'ascii'))

        # Get the folder name for the image size
        folder = str(self.request.recv(BUFFER_SIZE), 'ascii')
        response = bytes("{}".format(getFiles(folder)), 'ascii')
        self.request.sendall(response)

        file = str(self.request.recv(BUFFER_SIZE), 'ascii')
        with open("files/" + folder + "/" + file, "rb") as f:
            pck = f.read(BUFFER_SIZE)
            while pck:
                self.request.send(pck)
                pck = f.read(BUFFER_SIZE)
