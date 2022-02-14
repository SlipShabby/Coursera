import socket
import time

from collections import defaultdict

class ClientError(Exception):
    pass

class Client:

    def __init__(self, ip, port, timeout = None):
        self.ip = ip
        self.port = port
        self.timeout = timeout

        try:
            self.connection = socket.create_connection((ip, port), timeout)
        except socket.error as err:
            raise ClientError("Can not establish connection", err)

    def put(self, key, value, timestamp):
        try:
            self.connection.sendall(f'put {key} {value} {timestamp}\n'.encode())
        except socket.error as err:
            raise ClientError("Put error", err)

        str1 = b''

        while (str1[len(str1) - 2: len(str1)] != b'\n\n'):
            try:
                str1 += self.connection.recv(1024)
            except socket.error as err:
                raise ClientError("Put error", err)

        serv, lines = str1.decode().split("\n",1)

        if (serv != 'ok'):
            raise ClientError("Server error")

    def get(self, key):
        try:
            self.connection.sendall(f"get {key}\n".encode())
        except socket.error as err:
            raise ClientError("Get error")

        str1 = b''

        while (str1[len(str1)-2 : len(str1)] != b'\n\n'):
            try:
                str1 += self.connection.recv(1024)
            except socket.error as err:
                raise ClientError('Error', err)

        serv, lines = str1.decode().split("\n", 1)

        if (serv != 'ok'):
            raise ClientError("Server Error")

        lines = lines.rstrip()

        dic = {}

        if (lines == ''):
            return dic
        
        lines = lines.split('\n')

        for line in lines:
            key, value, timestamp = line.split()

            value = float(value)
            timestamp = int(timestamp)

            if (not key in dic):
                dic[key] = []
            dic[key].append((timestamp, value))

        return dic


if (__name__ == "__main__"):
	client = Client("127.0.0.1", 8888, timeout=15)

	client.put("palm.cpu", 0.5, timestamp=1150864247)
	client.put("palm.cpu", 2.0, timestamp=1150864248)
	client.put("palm.cpu", 0.5, timestamp=1150864248)

	client.put("eardrum.cpu", 3, timestamp=1150864250)
	client.put("eardrum.cpu", 4, timestamp=1150864251)
	client.put("eardrum.memory", 4200000)

	print(client.get("*"))
    