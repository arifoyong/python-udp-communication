import argparse
import socket
import socketserver

class MyUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        addr, port = self.client_address
        bytesData = self.request[0].strip()
        data = bytesData.decode('utf-8')
        print("{}:{} - {}".format(addr, port, data))
 
def main(host,port):
    if host == 'localhost':
        host = socket.gethostname()
    print("UDP server up and listening on {}:{}".format(host, port))
    with socketserver.UDPServer((host, port), MyUDPHandler) as server:
        server.serve_forever()

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--host', action='store', type=str,  default='localhost')
    my_parser.add_argument('--port', action='store', type=int,  default='10000')

    args = my_parser.parse_args()
    main(args.host, args.port)
