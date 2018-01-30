import subprocess
 
host = raw_input("Enter a host to map: ")
print(host)
 
p1 = subprocess.Popen(['nmap', '-O', host], stdout=subprocess.PIPE)
 
output = p1.communicate()[0]
 
print(output)

"""
Starting Nmap 6.40 ( http://nmap.org ) at 2018-01-30 23:05 CST
Nmap scan report for 192.168.1.1
Host is up (0.0018s latency).
Not shown: 955 filtered ports, 43 closed ports
PORT     STATE SERVICE
80/tcp   open  http
1900/tcp open  upnp
MAC Address: 14:E6:E4:5C:1A:90 (Tp-link Technologies CO.)
Device type: general purpose
Running: Wind River VxWorks
OS CPE: cpe:/o:windriver:vxworks
OS details: VxWorks
Network Distance: 1 hop

OS detection performed. Please report any incorrect results at http://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 6.41 seconds

"""d