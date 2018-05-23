import socket
from OpenSSL import SSL


class Server:
    def __init__(self, port):
        # SSL Initialize context
        context = SSL.Context(SSL.SSLv23_METHOD)
        context.use_privatekey_file('server.key')
        context.use_certificate_file('server.crt')

        self.sock = SSL.Connection(context, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        self.sock.bind(('', port))
        self.sock.settimeout(5)

        self.sock.listen(5)

        while True:
            (connection, address) = self.sock.accept()
            print(connection.recv(65535))


if __name__ == '__main__':
    server = Server(6666)
