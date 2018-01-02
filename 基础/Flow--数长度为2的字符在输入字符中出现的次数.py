def findstr(find, inputed):
        count = 0
        length = len(inputed)
        if find not in inputed:
            print("在目标字符串中未找到字符串！")
        else:
            for each in range (length-1):
                if inputed[each] == find[0] and inputed[each+1] == find[1]:
                    count +=1        
            print("子字符串在目标字符串中共出现%d次" % count)

while True:  
	inputed = str(input("请输入目标字符串："))
    find = "1212121"
    while len(find) != 2:
        find = str(input("请输入子字符串（两个字符）："))
    findstr(find, inputed)
    print ("\n")
