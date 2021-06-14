import socketserver
import argparse

class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        msg = self.data.decode('utf-8')
        ip, port = self.client_address
        print("{}:{} - {}".format(ip, port, msg))

def main(host, port):
    print(">> Listening on {}:{}  (press Ctrl+C to interrupt)".format(host, port))

    # Create the server & bind to host:port
    with socketserver.TCPServer((host, port), MyTCPHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--host', action='store', type=str,  default='localhost')
    my_parser.add_argument('--port', action='store', type=int,  default='10000')

    args = my_parser.parse_args()
    main(args.host, args.port)