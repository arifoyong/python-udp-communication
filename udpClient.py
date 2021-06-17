import socket
import argparse

BUFFER_SIZE = 1042

def main(host, port):
    print("Trying to send to {}:{}".format(host, port))
    data = ""
    UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

    while data !="exit":
        data = input()
        bytesToSend = str.encode(data)
        UDPClientSocket.sendto(bytesToSend, (host, port))

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--host', action='store', type=str,  default='10.28.16.92')
    my_parser.add_argument('--port', action='store', type=int,  default='10000')

    args = my_parser.parse_args()
    main(args.host, args.port)