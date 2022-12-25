#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set sw=4 ts=4 fdm=indent fdl=0 fdn=2 ft=python et:

from __future__ import print_function, division

import zmq
import socket

context = zmq.Context()

def send_test_message():
    socket = context.socket(zmq.STREAM)

    socket.connect('tcp://localhost:5555')
    id_sock = socket.getsockopt(zmq.IDENTITY)
    socket.send(id_sock, zmq.SNDMORE)
    socket.send(b'message')

def recv_test_message():
    socket = context.socket(zmq.STREAM)

    socket.bind('tcp://*:5555')
    id_sock = socket.recv()
    assert not socket.recv()    # empty data here
    assert socket.recv() == id_sock
    message = socket.recv()
    print('received:', message)


def test_from_zmq_to_socket():
    # Ordering of bind/connect matters!
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(('localhost', 5557))
    listener.listen(5)

    zsock = context.socket(zmq.STREAM)
    zsock.connect("tcp://localhost:5557")
    id_sock = zsock.getsockopt(zmq.IDENTITY)
    print("Identity", zsock.recv())  
    print("Empty", zsock.recv())

    zsock.send(id_sock, zmq.SNDMORE)
    zsock.send(b"Message from zsock 1")

    sock, _ = listener.accept()
    print(sock.recv(35))

    sock.send(b"Message from sock 1")
    print(1, zsock.recv())
    print(2, zsock.recv())
    
    zsock.send(id_sock, zmq.SNDMORE)
    zsock.send(b"Message from zsock 2")
    print(sock.recv(35))
    sock.send(b"Message from sock 2")
    print(1, zsock.recv())
    print(2, zsock.recv())

    zsock.send(id_sock, zmq.SNDMORE)
    zsock.send(b"Message from zsock 3")
    print(sock.recv(35))
    sock.send(b"Message from sock 3")
    print(1, zsock.recv())
    print(2, zsock.recv())

    sock.close()
    zsock.close()
    listener.close()

def test_from_zmqs_to_socket():
    # REMARK: Ordering of bind/connect matters!
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind(('localhost', 5557))
    listener.listen(5)

    zsock1 = context.socket(zmq.STREAM)
    zsock1.connect("tcp://localhost:5557")
    id_sock1 = zsock1.getsockopt(zmq.IDENTITY)
    print("Identity", zsock1.recv())  
    print("Empty", zsock1.recv())
    zsock1.send(id_sock1, zmq.SNDMORE)
    zsock1.send(b"Message from zsock1 1")

    zsock2 = context.socket(zmq.STREAM)
    zsock2.connect("tcp://localhost:5557")
    id_sock2 = zsock2.getsockopt(zmq.IDENTITY)
    print("Identity", zsock2.recv())  
    print("Empty", zsock2.recv())
    zsock2.send(id_sock2, zmq.SNDMORE)
    zsock2.send(b"Message from zsock2 1")

    sock1, _ = listener.accept()
    sock2, _ = listener.accept()
    print(1, sock1.recv(35))
    print(2, sock2.recv(35))

    sock1.send(b"Message from sock1 1-1")
    sock1.send(b"Message from sock1 1-2")
    sock2.send(b"Message from sock2 1")
    print(1, zsock1.recv())
    print(1, zsock1.recv())
    
    zsock1.send(id_sock1, zmq.SNDMORE)
    zsock1.send(b"Message from zsock1 2")
    print(sock1.recv(35))
    sock1.send(b"Message from sock1 2")
    print(1, zsock1.recv())
    print(1, zsock1.recv())

    print(2, zsock2.recv())
    print(2, zsock2.recv())
    sock1.close()
    zsock1.close()
    zsock2.close()
    listener.close()

def test_from_socket_to_zmq():
    zsock = context.socket(zmq.STREAM)
    zsock.bind("tcp://127.0.0.1:5557")

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', 5557))
    sock.send(b"Message from sock 1")

    print("Identity", zsock.recv())
    print("Empty", zsock.recv())

    id_sock = zsock.getsockopt(zmq.IDENTITY)
    zsock.send(id_sock, zmq.SNDMORE)
    zsock.send(b"Message from zsock 1")
    print(sock.recv(35))

    sock.send(b"Message from sock 2")
    print("Identity", zsock.recv())
    print("Message", zsock.recv())
    zsock.send(id_sock, zmq.SNDMORE)
    zsock.send(b"Message from zsock 2")

    sock.close()
    zsock.close()

# def test_close_zmq_from_socket():


if __name__ == '__main__':
    test_from_zmqs_to_socket()
    # test_from_socket_to_zmq()

    context.term()
