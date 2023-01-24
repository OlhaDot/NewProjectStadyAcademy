import socket

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen()
    conn, addr = s.accept()
    print('Server was started')
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            if data.decode('UTF-8') == '0':
                var = 'process failed'
            else:
                var = 'process is finished successfully'
            conn.send(bytes(var, encoding='UTF-8'))
