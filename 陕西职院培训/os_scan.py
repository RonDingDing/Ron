import subprocess
 
host = input("Enter a host to map: ")
 
p1 = subprocess.Popen(['nmap', '-O', host], stdout=subprocess.PIPE)
 
output = p1.communicate()[0]
 
print(output)