# task 1 -  loging
import logging
import socket

logging.basicConfig(filename='lesson11_server.log', level=logging.INFO)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))
    s.listen()

    logging.info('Server started, listening on port 5000')

    while True:
        conn, addr = s.accept()
        with conn:
            # logging.info('Connection established from {addr}')
            data = conn.recv(1024)
            data_dec = data.decode('UTF-8')
            if data_dec == '1':
                var = 'process is finished successfully'
                conn.send(bytes(var, encoding='UTF-8'))
                logging.info('process is finished successfully')
            elif data_dec == '0':
                var = 'process is not finished successfully'
                conn.send(bytes(var, encoding='UTF-8'))
                logging.warning('process is not finished successfully, but process is gong on')
            else:
                logging.error('Error - wrong format of data from client')
                break

print()
# task 2 - tests pytest
from lesson14 import Tree
import sys

print("---------------tests----------")

# add_node
def test_add_node():
    tree = Tree()
    tree.add_node(10)
    assert tree.root.val == 10

    tree.add_node(5)
    assert tree.root.left.val == 5

    tree.add_node(15)
    assert tree.root.right.val == 15

    tree.add_node(2)
    assert tree.root.left.left.val == 2

    tree.add_node(7)
    assert tree.root.left.right.val == 7

    tree.add_node(12)
    assert tree.root.right.left.val == 12

    tree.add_node(20)
    assert tree.root.right.right.val == 20

# min max test
def test_find_min():
    tree = Tree()
    assert tree.find_min() is None

    tree.add_node(10)
    assert tree.find_min() == 10

    tree.add_node(5)
    assert tree.find_min() == 5

    tree.add_node(15)
    assert tree.find_min() == 5

    tree.add_node(2)
    assert tree.find_min() == 2

    tree.add_node(7)
    assert tree.find_min() == 2

    tree.add_node(12)
    assert tree.find_min() == 2

    tree.add_node(20)
    assert tree.find_min() == 2


def test_find_max():
    tree = Tree()
    assert tree.find_max() is None

    tree.add_node(10)
    assert tree.find_max() == 10

    tree.add_node(5)
    assert tree.find_max() == 10

    tree.add_node(15)
    assert tree.find_max() == 15

    tree.add_node(2)
    assert tree.find_max() == 15

    tree.add_node(7)
    assert tree.find_max() == 15

    tree.add_node(12)
    assert tree.find_max() == 15

    tree.add_node(20)
    assert tree.find_max() == 20

# remove
def test_remove_node():
    tree = Tree()
    tree.remove_node(10)
    assert tree.root is None

    tree.add_node(10)
    tree.remove_node(10)
    assert tree.root is None

    tree.add_node(10)
    tree.add_node(5)
    tree.add_node(15)
    tree.remove_node(20)
    assert tree.root.right is None

    tree.remove_node(5)
    assert tree.root.left.val == 10
    assert tree.root.left.left is None
    assert tree.root.left.right is None

    tree.add_node(2)
    tree.add_node(7)
    tree.add_node(12)
    tree.add_node(20)
    tree.remove_node(10)
    assert tree.root.val == 12
    assert tree.root.left.val == 5
    assert tree.root.left.left.val == 2
    assert tree.root.left.right.val == 7
    assert tree.root.right.val == 15
    assert tree.root.right.right.val == 20
