import os
import Crypto
from Crypto.Util import Padding
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import socket

IP = '192.'
PORT = 5037
ADDR = (IP, PORT)
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(ADDR)

    # send request of many files
    file_names = []

    for filename in file_names:
        # Sending the filename to the server.
        client.send(filename.encode("utf-8"))

        # Receive data from server, ready to send encrypted files to client
        msg = client.recv(SIZE).decode("utf-8")
        print(f"[SERVER]: {msg}")

        # Opening and reading the file data in binary
        file = open(filename, "rb")
        # decrypt files

        data = file.read()

        # Sending the file data to the server.
        client.send(data)

        # Closing the file.
        file.close()

        # Receive data from server
        msg = client.recv(SIZE).decode("utf-8")
        print(f"[SERVER]: {msg}")

    # Closing the connection from the server.
    client.close()


if __name__ == "__main__":
    main()

