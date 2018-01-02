import os.path
import os

def filecopy(file_name):
	f = open(file_name)
	f2 = open("replacer.txt", "w")

	for each_line in f:
		each_line = each_line.lower()         # 全部转变成小写
		f2.writelines(each_line)
		  									# 复制一个小写般的文件replacer.txt
	f.close()
	f2.close()


def findlemma(file_name):	
	origin_word = input("请输入需要查找的词/标点符号:").lower()
	lemma = [origin_word, ]

	while True:
		baby = input("请输入需要查找的词/标点符号的变体，输入:s结束：")
		bab = baby.lower()
		lemma.append(bab)
		if baby == ":s":
			break   
			             #输入要查找的词及其变体
	lemma.remove(":s")
	for each in lemma:
		if "" in lemma:
			lemma.remove("")   


	if origin_word == "":
		print("\n程序重新运行\n")
		findlemma(file_name1)
	else:
		lemma = list(set(lemma))
	 	 				#整理词库，删除多余项和":s"

	
	content = []

	f3 = open("replacer.txt")
	for each_lino in f3:
		for each_word in lemma:
			if each_word or origin_word in each_lino:
				each_lino = each_lino.replace(each_word, origin_word)
				content.append(each_lino)

	

	content2 = []

	for a in range(len(content)):
		if (a+1) % len(lemma) == 0:		#循环后会生成原文行数乘以lemma个数的行
			content2.append(content[a]) #每隔lemma数为一组
			    					    #每组最后一个为全部已替换的
			    					    #把这样的句子添加到新列表当中

	f3.close()


	count = 0
	shu = []

	f4 = open("replacer1.txt","w")
	f4.writelines(content2)
	f4.close()



	f5 = open("replacer1.txt")
	listfile = []
	listline = []

	for each_lini in f5:
		listfile.append(each_lini)
	numline = len(listfile)

	f5.seek(0,0)
	       # 指针归位！！！
	for each_lina in f5:
		if origin_word in each_lina:
			count += each_lina.count(origin_word)
			listline.append(each_lina.count(origin_word))

	f5.close()

	print("全文有%s行" % numline)
	print("%s及其变体" % origin_word, end="")
	for m in range(len(lemma)-1):
		print (lemma[m], end= '|')
	print("共有%s个" % count)

	for each_content in range(0, numline):
		print ("第%s行共有%s个%s及其变体" % (each_content+1, listline[each_content], origin_word))




	
	filepath = os.path.dirname(file_name)
	if filepath == "":
		filepath = os.curdir
	os.chdir(filepath)
	os.remove("replacer1.txt")
	os.remove("replacer.txt")   #删除留有的replacer、replacer1.txt


while True:
	print("\n程序重新运行\n")
	file_name1 = input("请输入要打开的文件：")
	if os.path.isfile(file_name1):
		break
filecopy(file_name1)
findlemma(file_name1)
 

