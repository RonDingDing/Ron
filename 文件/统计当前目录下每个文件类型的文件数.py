import os
import os.path

filecount = 0
baby = []
os.getcwd()                      #获取当前目录
filelist = os.listdir(os.curdir) #打印当前文件及文件夹
for eachfile in filelist:        #逐个判断是否存在且是一个目录
	if os.path.isdir(eachfile) == True:   
		filecount += 1           #如是，文件夹数目+1
for eachfile in filelist: 
	if os.path.isfile(eachfile) == True: #逐个判断是否存在且是一个文件
		(filename, extension) = os.path.splitext(eachfile)       #如是，分割文件名
		baby.append(extension)
 
filetype = set (baby)
filetypenumber = len(filetype)

diamond = []
for eachmember in filetype:
	eachmembernumber = baby.count(eachmember)
	diamond.append([eachmember, eachmembernumber])

print("当前目录是："+ str(os.getcwd()))
for sick in range(len(diamond)):
	print ("共有"+str(diamond[sick][0])+"文件"+str(diamond[sick][1])+"个")
print ("共有文件夹" + str(filecount) + "个")

input()
