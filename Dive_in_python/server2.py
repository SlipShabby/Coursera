import asyncio

metrics_dict = dict()


class ClientServerProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        resp = process_data(data.decode())
        self.transport.write(resp.encode())

def run_server(host, port):
    loop = asyncio.get_event_loop()
    coro = loop.create_server(ClientServerProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()

def process_data(data):
    good = 'ok\n\n'
    wron_cmd = 'error\nwrong command\n\n'
    index_error = 'Index error'

    if data.strip('\n').strip() == '':
        return wron_cmd

    command = data.split()

    if command[0] == 'get':
        if len(command) == 2:
            send_metrics = 'ok\n'
            key = command[1]
            if key == '*':
                for key, item_list in metrics_dict.items():
                    item_list.sort()
                    for item_tuple in item_list:
                        try:
                            send_metrics += f'{key} {item_tuple[1]} {item_tuple[0]}\n'
                        except IndexError:
                            return index_error
                return send_metrics + '\n'

            metrics_list = metrics_dict.get(key, None)
            if metrics_list is None:
                return good

            try:
                metrics_list.sort()
                for metric in metrics_list:
                    send_metrics += f'{key} {metric[1]} {metric[0]}\n'
                return send_metrics + '\n'
            except IndexError:
                return index_error

        else:
            return wron_cmd

    elif command[0] == 'put':
        if len(command) == 4:
            try:
                key, value, timestamp = command[1], float(command[2]), int(command[3])
            except ValueError:
                return wron_cmd

            old_metrics_list = metrics_dict.get(key, [])
            for i, metric in enumerate(old_metrics_list):
                if metric[0] == timestamp:
                    old_metrics_list.remove((timestamp, metric[1]))
                    old_metrics_list.insert(i, (timestamp, value))
                    return good

            old_metrics_list.append((timestamp, value))
            metrics_dict.update({key: old_metrics_list})
            return good
        else:
            return wron_cmd

    else:
        return wron_cmd


if __name__ == '__main__':
    run_server('127.0.0.1', 8888)