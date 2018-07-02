#!/usr/bin/python

import socket
import sys

# create the socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get the hostname
host = socket.gethostname()

# set the port
port = 9999

# connect the service
s.connect((host, port))

# accept the less than 1024bit
msg = s.recv(1024)

s.close()

print(msg.decode("utf-8"))
