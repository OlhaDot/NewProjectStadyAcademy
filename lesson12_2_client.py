# 2 - server socket
# client for server socket check
import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(('localhost', 55000))
    s.send(bytes('-2,4', encoding='UTF-8'))

