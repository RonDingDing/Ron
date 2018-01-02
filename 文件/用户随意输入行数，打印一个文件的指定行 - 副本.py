def openfile():
	file_name =  input("请输入需要打开的文件，（C:/test.txt）:")
	listfile = list(open(file_name))
	lenlist = int(len(listfile))
	

	hang = ""
	hanglist = list(hang.split(":"))
	
	while len(hanglist) !=2:
		hang = input("请输入需要显示的行数【格式如:3, 2:, 1:3】：")
		hanglist = list(hang.split(":"))

	starting = (hanglist[0])
	ending = (hanglist[1])

	


	if starting == "" or "0":
		starting = 1
		differ = 1
		
	if ending == "":
		ending = lenlist
		differ = 2

	else: 
		differ = 3

	print (starting, ending)
	print (differ)

	startin = int(starting)
	endin = int(ending)
	starting = abs(startin)
	ending = abs(endin)
	

	if starting > lenlist:
		starting = lenlist
	if ending > lenlist:
		ending = lenlist
	if starting > ending:
		huan = starting
		starting = ending
		ending = huan

	if differ == 1:
		prompt = "从开始到第%s行" % ending
	elif differ == 2:
		prompt = "从第%s行到结束" % (starting+1)
	elif differ == 3:
		prompt = "从第%s行到第%s行" % (starting, ending)

	
	print("文本%s共有%s行。" % (file_name, lenlist))
	print(prompt + "的文本为：" + "\n\n")

	for eachline in range(starting, ending):
		print(eachline)
	
		





openfile()




