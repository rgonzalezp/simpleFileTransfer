import threading
import socketserver
import clientHandler


class FileServer(socketserver.ThreadingTCPServer):
    """docstring for FileServer"""

    def __init__(self, address, handler, max_clients=1):
        super().__init__(address, handler)
        self.current_clients = 0
        self.max_clients = max_clients

    def service_actions(self):
        self.current_clients = threading.active_count() - 1
        print(self.current_clients)

    def verify_request(self, request, client_address):
        if self.current_clients == self.max_clients:
            return False
        else:
            return True


if __name__ == "__main__":
    # Port 0 means to select an arbitrary unused port
    HOST, PORT = "localhost", 27000

    server = FileServer((HOST, PORT), clientHandler.Handler)
    ip, port = server.server_address

    # Start a thread with the server -- that thread will then start one
    # more thread for each request
    try:
        print("Server loop running in thread")
        server.serve_forever()
    except KeyboardInterrupt:
        print("Forced server to close")
    finally:
        server.shutdown()
