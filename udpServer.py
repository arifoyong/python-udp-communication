import socketserver
import argparse

BUFFER_SIZE = 1024

class udpHandler(socketserver.BaseRequestHandler):
    # Receive udp packet & print to console
    def handle(self):
        self.data = self.request.recv(BUFFER_SIZE).strip()
        msg = self.data.decode('utf-8')
        ip, port = self.client_address
        print("{}:{} - {}".format(ip, port, msg))

def main(host, port):
    print(">> Listening on {}:{}  (press Ctrl+C to interrupt)".format(host, port))
    with socketserver.TCPServer((host, port), udpHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--host', action='store', type=str,  default='localhost')
    my_parser.add_argument('--port', action='store', type=int,  default='10000')

    args = my_parser.parse_args()
    main(args.host, args.port)
