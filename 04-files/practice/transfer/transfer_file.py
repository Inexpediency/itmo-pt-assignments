import json
import pathlib
import pickle
import socket
import zlib

HOST = '127.0.0.1'
PORT = 65432


def run_receiver(target_directory):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = b''
            received = conn.recv(2**10)
            while received:
                data += received
                received = conn.recv(2**10)

            data = pickle.loads(data)
            filename = data['filename']
            file_data = data['data']
            with open(f'{target_directory}/{filename}', 'wb') as f:
                f.write(file_data)


def run_sender(source_file):
    filename = source_file.split('/')[-1]
    with open(source_file, 'rb') as f:
        file_data = f.read()

    data = {
        'filename': filename,
        'data': file_data
    }

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(pickle.dumps(data))
