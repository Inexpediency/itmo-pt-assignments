import pickle
import socket

HOST = '127.0.0.1'
PORT = 65433


def run_receiver():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            data = conn.recv(2**20)
            return pickle.loads(data)


def run_sender(obj):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.send(pickle.dumps(obj))
