# -*- coding: utf-8 -*-

#server
import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 8089))
sock.listen(2)
try:
    #while True:
    conn, addr = sock.accept()
    data = conn.recv(1024).decode("ascii")
    print(data)
    conn.send("hi from server".encode())
        # sock.send('this will cause broken pipe error.'.encode())
except Exception as e:
    print('except by:',e)
finally:
    sock.close()
