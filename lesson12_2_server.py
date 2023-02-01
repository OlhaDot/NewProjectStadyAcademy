#2.socket server
# socket server
import socket
import asyncio

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(1)
print('Server is running, please, press ctrl+c to stop')

conn, addr = sock.accept()
print('connected:', addr)
data = conn.recv(1024)
data_dec = data.decode('UTF-8')
separated = data_dec.split(',')
x = int(separated[0])
y = int(separated[1])

async def task1_sum(x, y):
    print('sum of numbers {} and {} = {}'.format(x, y, x + y))
    await asyncio.sleep(1)


async def task2_diff(x, y):
    print('diff between numbers {} and {} = {}'.format(x, y, x - y))
    await asyncio.sleep(1)


async def task3_multipl(x, y):
    print('multiple of numbers {} and {} = {}'.format(x, y, x * y))
    await asyncio.sleep(1)


if __name__ == '__main__':
    ioloop = asyncio.new_event_loop()
    tasks = [
        ioloop.create_task(task1_sum(x, y)),
        ioloop.create_task(task2_diff(x, y)),
        ioloop.create_task(task3_multipl(x, y))]

    ioloop.run_until_complete(asyncio.wait(tasks))
    ioloop.close()
