import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 65432))
    s.send(bytes('1', encoding='UTF-8'))
    data = s.recv(1024)

print("Received {}".format(data))