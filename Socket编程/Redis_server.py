#!/usr/bin/env python
# coding=utf-8
import socket

a = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
a.bind(('localhost', 7665))

while True:
    data, addr = a.recvfrom(1024)
    if data:
        print(data)
