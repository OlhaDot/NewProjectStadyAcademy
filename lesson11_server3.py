import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('127.0.0.1', 45000))
    s.listen()
    conn, addr = s.accept()
    print('Server was started')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            spaces = 1
            for char in data.decode('UTF-8'):
                if char == ' ':
                    spaces += 1
            conn.send(bytes(str(spaces)+" words in your sentence", encoding='UTF-8'))
