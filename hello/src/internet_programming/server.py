#!/usr/bin/python

# import the modules: socket, sys
import socket
import sys

# create the socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the localhost name
host = socket.gethostname()

port = 9999

# bind the port
serversocket.bind((host, port))

# set the max connections, queuing after passing
serversocket.listen(5)

while True:
    # establish connection to client
    clientsocket, addr = serversocket.accept()

    print("连接地址：%s" % str(addr))

    msg = "欢迎访问菜鸟教程！" + "\r\n"

    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()
