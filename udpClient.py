import socket
import argparse

def main(host, port):
    data = ""
    print(">> Connecting to {}:{}  (type exit to quit program)".format(host, port))
    while data != 'exit':
        data = input()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))
            sock.sendall(bytes(data, "utf-8"))

if __name__ == "__main__":
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--host', action='store', type=str,  default='localhost')
    my_parser.add_argument('--port', action='store', type=int,  default='10000')

    args = my_parser.parse_args()
    main(args.host, args.port)