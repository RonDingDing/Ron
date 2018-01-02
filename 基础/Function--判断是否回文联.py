def panlidrome(sentence):
    r = str(sentence)
    le = len(r)
    t = 0
    for each in range(le):
        if r[each] == r[-(each + 1)]:
            t = 1            
        else:
            break
            t = 0
        if t == 1:
            print ("是回文联！")
        if t == 0:
            print ("不是回文联！")
            
while True:
	sentence = input("请输入一句话：")
    panlidrome(sentence)
    print ("\n")

