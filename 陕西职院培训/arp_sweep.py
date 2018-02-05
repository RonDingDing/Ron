#!/usr/bin/env python

import ipcalc
import sys

from arprequest import ArpRequest

n = '172.16.6.136'
lfile = '999.txt'

try:
    iface = sys.argv[3]
except:
    iface = 'eth0'

net = ipcalc.Network(n)
print(net)

with open(lfile, 'w') as f:
    for ip in net:
        f.write('{} '.format(ip))
        sys.stdout.write('{} '.format(ip))

        req = ArpRequest(str(ip), iface)
        if not req.request():
            f.write('Not ')
            sys.stdout.write('Not ')
        f.write('Used\n')
        sys.stdout.write('Used\n')
