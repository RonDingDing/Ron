import os
import os.path
def searchfile(startpath):
	os.chdir(startpath)
	content = []
	lable = ["mp4","rmvb","avi"]
	filelist = os.listdir(os.curdir)
	print(filelist)
	for eachfile in filelist:
		if os.path.isfile(eachfile) == True: #如果是文件，就分离扩展名
			yuanzu = os.path.splitext(eachfile)#扩展名在lable里，得到路径
			if yuanzu[1] in lable:
				content.append(os.getcwd() + os.sep + each_file)  
		elif os.path.isdir(eachfile) == True: #如果是文件夹，往下走
			searchfile(eachfile)
			os.chdir(os.pardir)	



	os.chdir(startpath)
	f = open("videolist.txt","w")
	f.writelines(content)
	f.close()


startpath = input("请输入起始路径：")
searchfile(startpath)

