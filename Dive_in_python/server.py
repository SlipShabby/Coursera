import asyncio

metrics = dict()


class ClientServerProtocol(asyncio.Protocol):

    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        response = process_data(data.decode())
        self.transport.write(response.encode())

def process_data(data):
    received = 'ok\n\n'
    wrong_cmd = 'error\n\n'
    index_error = 'Index Error'

    if data.strip('\n').strip() == '':
        return wrong_cmd

    cmd = data.split()

    if cmd[0] == 'put':
        if len(cmd) == 4:
            try: 
                key, value, timestamp = cmd[1], float(cmd[2]), int(cmd[3])
            except ValueError:
                return wrong_cmd

                old_metrics = metrics.get(key, [])
                for i, metric in enumerate(old_metrics):
                    if metric[0] == timestamp:
                        old_metrics.remove((timestamp, metric[1]))
                        old_metrics.insert(i, (timestamp, value))
                        return received

                old_metrics.append((timestamp, value))
                metrics.update({key: old_metrics})
                return received
        else:
            return wrong_cmd

    elif cmd[0] == 'get':
        if len(cmd) == 2:
            send_metrics = 'ok\n'
            key = cmd[1]
            if key == '*':
                for key, item_list in metrics.items():
                    item_list.sort()
                    for item_tuple in item_list:
                        try:
                            send_metrics += f'{key} {item_tuple[1]} {item_tuple[0]}\n'
                        except IndexError:
                            return index_error

                return send_metrics + '\n''

            metrics_list = metrics.get(key, None)
            if metrics_list is None:
                return received

            try:
                metrics_list.sort()
                for metric in metrics_list:
                    send_metrics += f'{key} {metric[1]} {metric[0]}\n'
                return send_metrics + '\n''
        else:
            return wrong_cmd

    else:
        return wrong_cmd

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol,host, email)
    server = loop.run_until_complete(coro)

    try: 
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)