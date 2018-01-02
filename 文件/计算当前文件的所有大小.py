import os
import os.path

filecount = 0
info = []
os.getcwd()                      
filelist = os.listdir(os.curdir)


for eachfile in filelist:
	filesize = os.path.getsize(eachfile)
	info.append([eachfile, filesize])

print("本文件夹下的文件信息如下：\n")

for eachcunt in info:
	a=eachcunt[0] 
	b=eachcunt[1] 
	print ("%-40s 大小：%20d" % (a,b))
