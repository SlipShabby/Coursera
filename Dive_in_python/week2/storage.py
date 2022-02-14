import os
import tempfile
import argparse
import json

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

def get_data():
    try:
        with open(storage_path, 'r') as f:
            return json.load(f)
    except:
        return {}
    return {}   

# def print_data(path, key):
#     data = get_data()
#     if key in data:
#         print(data.get(key))
def print_data(path, key):
    data = get_data()
    if data:
        if key in data:
            ret = data.get(key)
            # if len(ret) == 1:
            #     print(ret[0])
            # else:
            #     print(ret)
            print(', '.join(ret))
    else:
        return None

def write_data(path, key, value):
    data = get_data()
    # print(data)
    if key in data:
        data[key].append(value)
        # print("1")
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        json.dump(data, f)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--key", help = "key value", type = str, default = None, dest = "key")
    parser.add_argument("--val", help = "value", type = str, default = None, dest = "val")
    args = parser.parse_args()
    if args.val is None:
        print_data(storage_path, args.key)
    else:
        write_data(storage_path, args.key, args.val)