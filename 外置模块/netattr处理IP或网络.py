点击(此处)折叠或打开
>>> ip=IPNetwork('10.10.10.2/25')
>>> ab=IPNetwork('10.10.10.200/25')
>>> ip.network
IPAddress('10.10.10.0')
>>> ab.network
IPAddress('10.10.10.128')
>>> ab=IPNetwork('10.10.10.130/25')
>>> ab.network
IPAddress('10.10.10.128')
>>> ab.network == ip.network
False
>>>

下面是netaddr的一些基本用法
点击(此处)折叠或打开
>>> from netaddr import *
>>> import pprint
>>> ip=IPAddress('192.168.1.1')
>>> ip.version
4
>>> repr(ip)
"IPAddress('192.168.1.1')"
>>> ip
IPAddress('192.168.1.1')
>>> str(ip)
'192.168.1.1'
>>> '%s' % ip
'192.168.1.1'
>>> ip.format()
'192.168.1.1'
>>> int(ip)
3232235777
>>> hex(ip)
'0xc0a80101'
>>> ip.bin
'0b11000000101010000000000100000001'
>>> ip.bits()
'11000000.10101000.00000001.00000001'
>>> ip.words
(192, 168, 1, 1)
>>> ip.network, ip.broadcast
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'IPAddress' object has no attribute 'network'
>>> ip=IPNetwork('192.0.2.1')
>>> ip.op
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'IPNetwork' object has no attribute 'op'
>>> ip.ip
IPAddress('192.0.2.1')
>>> ip.network,ip.broadcast
(IPAddress('192.0.2.1'), IPAddress('192.0.2.1'))
>>> ip.netmask, ip.hostmask
(IPAddress('255.255.255.255'), IPAddress('0.0.0.0'))
>>> ip.size
1
>>> ip=IPNetwork('192.179.0.1/24')
>>> ip.ip
IPAddress('192.179.0.1')
>>> ip.network
IPAddress('192.179.0.0')
>>> ip.broadcast
IPAddress('192.179.0.255')
>>> ip.netmask,ip.hostmask
(IPAddress('255.255.255.0'), IPAddress('0.0.0.255'))
>>> ip=IPNetwork('0.0.0.0/0')
>>> ip
IPNetwork('0.0.0.0/0')
>>> ip.value=3221225985
>>> ip
IPNetwork('192.0.2.1/0')
>>> ip.prefixlen
0
>>> ip.prefixlen = 23
>>> ip
IPNetwork('192.0.2.1/23')
>>> ip.cidr
IPNetwork('192.0.2.0/23')
>>> ip.ip.bits()
'11000000.00000000.00000010.00000001'
>>> ip.network.bits()
'11000000.00000000.00000010.00000000'
>>> ip.netmask.bits()
'11111111.11111111.11111110.00000000'
>>> ip.broadcast.bits()
'11000000.00000000.00000011.11111111'
>>> import random
>>> ip_list=list(IPNetwork('192.0.2.198/28'))
>>> random.shuffle(ip_list)
>>> sorted(ip_list)
[IPAddress('192.0.2.192'), IPAddress('192.0.2.193'), IPAddress('192.0.2.194'), IPAddress('192.0.2.195'), IPAddress('192.0.2.196'), IPAddress('192.0.2.197'), IPAddress('192.0.2.198'), IPAddress('192.0.2.199'), IPAddress('192.0.2.200'), IPAddress('192.0.2.201'), IPAddress('192.0.2.202'), IPAddress('192.0.2.203'), IPAddress('192.0.2.204'), IPAddress('192.0.2.205'), IPAddress('192.0.2.206'), IPAddress('192.0.2.207')]
>>> ip_list=[ ip for ip in IPNetwork('fe80::/120')]
>>> ip=IPNetwork('172.24.0.0/16')
>>> ip.subnet(23)
<generator object subnet at 0x7f63d0615a00>
>>> subnets=list(ip.subnet(23))
>>> len(subnets)
128
>>> subnets
[IPNetwork('172.24.0.0/23'), IPNetwork('172.24.2.0/23'), IPNetwork('172.24.4.0/23'), IPNetwork('172.24.6.0/23'), IPNetwork('172.24.8.0/23'), IPNetwork('172.24.10.0/23'), IPNetwork('172.24.12.0/23'), IPNetwork('172.24.14.0/23'), IPNetwork('172.24.16.0/23'), IPNetwork('172.24.18.0/23'), IPNetwork('172.24.20.0/23'), IPNetwork('172.24.22.0/23'), IPNetwork('172.24.24.0/23'), IPNetwork('172.24.26.0/23'), IPNetwork('172.24.28.0/23'), IPNetwork('172.24.30.0/23'), IPNetwork('172.24.32.0/23'), IPNetwork('172.24.34.0/23'), IPNetwork('172.24.36.0/23'), IPNetwork('172.24.38.0/23'), IPNetwork('172.24.40.0/23'), IPNetwork('172.24.42.0/23'), IPNetwork('172.24.44.0/23'), IPNetwork('172.24.46.0/23'), IPNetwork('172.24.48.0/23'), IPNetwork('172.24.50.0/23'), IPNetwork('172.24.52.0/23'), IPNetwork('172.24.54.0/23'), IPNetwork('172.24.56.0/23'), IPNetwork('172.24.58.0/23'), IPNetwork('172.24.60.0/23'), IPNetwork('172.24.62.0/23'), IPNetwork('172.24.64.0/23'), IPNetwork('172.24.66.0/23'), IPNetwork('172.24.68.0/23'), IPNetwork('172.24.70.0/23'), IPNetwork('172.24.72.0/23'), IPNetwork('172.24.74.0/23'), IPNetwork('172.24.76.0/23'), IPNetwork('172.24.78.0/23'), IPNetwork('172.24.80.0/23'), IPNetwork('172.24.82.0/23'), IPNetwork('172.24.84.0/23'), IPNetwork('172.24.86.0/23'), IPNetwork('172.24.88.0/23'), IPNetwork('172.24.90.0/23'), IPNetwork('172.24.92.0/23'), IPNetwork('172.24.94.0/23'), IPNetwork('172.24.96.0/23'), IPNetwork('172.24.98.0/23'), IPNetwork('172.24.100.0/23'), IPNetwork('172.24.102.0/23'), IPNetwork('172.24.104.0/23'), IPNetwork('172.24.106.0/23'), IPNetwork('172.24.108.0/23'), IPNetwork('172.24.110.0/23'), IPNetwork('172.24.112.0/23'), IPNetwork('172.24.114.0/23'), IPNetwork('172.24.116.0/23'), IPNetwork('172.24.118.0/23'), IPNetwork('172.24.120.0/23'), IPNetwork('172.24.122.0/23'), IPNetwork('172.24.124.0/23'), IPNetwork('172.24.126.0/23'), IPNetwork('172.24.128.0/23'), IPNetwork('172.24.130.0/23'), IPNetwork('172.24.132.0/23'), IPNetwork('172.24.134.0/23'), IPNetwork('172.24.136.0/23'), IPNetwork('172.24.138.0/23'), IPNetwork('172.24.140.0/23'), IPNetwork('172.24.142.0/23'), IPNetwork('172.24.144.0/23'), IPNetwork('172.24.146.0/23'), IPNetwork('172.24.148.0/23'), IPNetwork('172.24.150.0/23'), IPNetwork('172.24.152.0/23'), IPNetwork('172.24.154.0/23'), IPNetwork('172.24.156.0/23'), IPNetwork('172.24.158.0/23'), IPNetwork('172.24.160.0/23'), IPNetwork('172.24.162.0/23'), IPNetwork('172.24.164.0/23'), IPNetwork('172.24.166.0/23'), IPNetwork('172.24.168.0/23'), IPNetwork('172.24.170.0/23'), IPNetwork('172.24.172.0/23'), IPNetwork('172.24.174.0/23'), IPNetwork('172.24.176.0/23'), IPNetwork('172.24.178.0/23'), IPNetwork('172.24.180.0/23'), IPNetwork('172.24.182.0/23'), IPNetwork('172.24.184.0/23'), IPNetwork('172.24.186.0/23'), IPNetwork('172.24.188.0/23'), IPNetwork('172.24.190.0/23'), IPNetwork('172.24.192.0/23'), IPNetwork('172.24.194.0/23'), IPNetwork('172.24.196.0/23'), IPNetwork('172.24.198.0/23'), IPNetwork('172.24.200.0/23'), IPNetwork('172.24.202.0/23'), IPNetwork('172.24.204.0/23'), IPNetwork('172.24.206.0/23'), IPNetwork('172.24.208.0/23'), IPNetwork('172.24.210.0/23'), IPNetwork('172.24.212.0/23'), IPNetwork('172.24.214.0/23'), IPNetwork('172.24.216.0/23'), IPNetwork('172.24.218.0/23'), IPNetwork('172.24.220.0/23'), IPNetwork('172.24.222.0/23'), IPNetwork('172.24.224.0/23'), IPNetwork('172.24.226.0/23'), IPNetwork('172.24.228.0/23'), IPNetwork('172.24.230.0/23'), IPNetwork('172.24.232.0/23'), IPNetwork('172.24.234.0/23'), IPNetwork('172.24.236.0/23'), IPNetwork('172.24.238.0/23'), IPNetwork('172.24.240.0/23'), IPNetwork('172.24.242.0/23'), IPNetwork('172.24.244.0/23'), IPNetwork('172.24.246.0/23'), IPNetwork('172.24.248.0/23'), IPNetwork('172.24.250.0/23'), IPNetwork('172.24.252.0/23'), IPNetwork('172.24.254.0/23')]
>>>


>>> a = netaddr.IPNetwork('10.0.0.0/30')
>>> l = list(a)
>>> l
[IPAddress('10.0.0.0'), IPAddress('10.0.0.1'), IPAddress('10.0.0.2'), IPAddress('10.0.0.3')]
>>> l.remove(netaddr.IPAddress('10.0.0.2'))
>>> l
[IPAddress('10.0.0.0'), IPAddress('10.0.0.1'), IPAddress('10.0.0.3')]
>> > c = netaddr.cidr_merge(l)
>> > c
[IPNetwork('10.0.0.0/31'), IPNetwork('10.0.0.3/32')]
>> > c
[IPNetwork('10.0.0.0/31'), IPNetwork('10.0.0.3/32')]
>> > for i in c:
  list(i)

[IPAddress('10.0.0.0'), IPAddress('10.0.0.1')]
[IPAddress('10.0.0.3')]
