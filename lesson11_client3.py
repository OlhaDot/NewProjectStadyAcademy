import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('127.0.0.1', 45000))
    s.send(bytes('This is a sentence', encoding='UTF-8'))
    data = s.recv(1024)

print("Received {}".format(data))