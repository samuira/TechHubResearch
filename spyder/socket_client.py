# -*- coding: utf-8 -*-
import socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect(("localhost",8089))
        # sock.setblocking(False) raise BlockingIOError exception
        sock.setblocking(False)
        sock.send("hi from client".encode())
        data = sock.recv(1024).decode("ascii")
        print(data)
    except BlockingIOError as e:
        print('except by BlockingIOError exception.',e)
    except Exception as e:
        print('run socket_server.py in a seperate terminal:',
              e.with_traceback)
    finally:
        sock.close()