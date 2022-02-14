import socket
import time

class ClientError(Exception):
    pass

class Client:

    def __init__(self, ip, port, timeout = None):
        self._ip = ip
        self._port = port
        self._timeout = timeout
        # try:
        #     self._sock = socket.create_connection((self._ip, self._port), self._timeout)
        # except socket.error as err:
        #     raise ClientError(err)

    def put(self, key, value, timestamp = None):
        if timestamp == None:
            timestamp = int(time.time())
        response = self.send(f'put {key} {value} {timestamp}\n')
        if response[0:3] != 'ok\n':
            raise ClientError(response)

    def get(self, key):
        response = self.send(f'get {key}\n')
        # print("response")

        if response[0:3] != 'ok\n':
            raise ClientError(response)

        result = dict()
        lines = response.split('\n')
        # print(key)

        for line in lines[1:-2]:
            metric = line.split(' ')
            if len(metric) == 3:
                response_key = metric[0]
                response_value = float(metric[1])
                response_timestamp = int(metric[2])
                
                response_l = result.get(response_key, [])
                response_l.append((response_timestamp, response_value))
                result.update({response_key: sorted(response_l)})
            elif metric not in [["ok"],[''],["'"]]:
                raise ClientError
        
        
        return result


    def send(self, cmd):
        try:
            self._sock = socket.create_connection((self._ip, self._port), self._timeout)
            # print("send")
            self._sock.sendall(cmd.encode('utf8'))
            # print("send2")
            buffer = self._sock.recv(1024)
            # print(buffer)
            return buffer.decode("utf-8")
        except socket.error as err:
            raise ClientError(err)

if __name__ == '__main__':
    client = Client('127.0.0.1', 8888, timeout=15)
    print(client.get('*'))