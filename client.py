import socket

from  OpenSSL import SSL


class Client:
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # self.sock.settimeout(5)

    def connect(self, server_addr, server_port):
        try:
            self.sock.connect((server_addr, server_port))
        except socket.error as error:
            print(f'Could not connect with the server: {error}')
        except TypeError as error:
            print(f'Type error: {error}')
        else:
            print(f'connected with {self.sock.getpeername()}')
            self.client_ssl = SSL.Connection(SSL.Context(SSL.SSLv23_METHOD), self.sock)
            self.client_ssl.set_connect_state()
            self.client_ssl.do_handshake()
            print(f'Server subject is{self.client_ssl.get_peer_certificate().get_subject()}')

    def send(self, message):
        self.client_ssl.send(message)

    def close(self):
        self.client_ssl.close()


if __name__ == '__main__':
    client = Client()
    client.connect('127.0.0.1', 6666)
    client.send('fuck')
    client.close()

