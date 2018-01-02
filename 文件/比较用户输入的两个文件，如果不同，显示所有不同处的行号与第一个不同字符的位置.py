def comparetext(file1, file2):
    f1 = open (file1)
    f2 = open (file2)
    count = 0
    f1lst = []
    f2lst = []
    differ = []

    f1lst = f1.readlines()
    f2lst = f2.readlines()

    f1len = int(len(f1lst))
    f2len = int(len(f2lst))

    print ("文件一有%d行。" % abs(f1len))
    print ("文件二有%d行。" % abs(f2len))

    if f1len < f2len:
        ginger = min(f1len, f2len)
        print ("两个文件行数不一，文件二多%d行。" % abs(f2len - f1len))
    elif f1len > f2len:
        ginger = min(f1len, f2len)
        print ("两个文件行数不一，文件一多%d行。" % abs(f2len - f1len))
    else:
        ginger = f1len
        print ("两个文件行数一致。")

    for count in range(0,ginger):
        if f1lst[count] != f2lst[count]:
            differ.append(count+1)

    if len(differ) == 0:
        print ("两个文件前%s行相同。" % ginger)
    else:
        print ("两个文件第%s行不同。" % differ)

while True:
    f1name = input("请输入需要比较的第一个文件：")
    f2name = input("请输入需要比较的另一个文件：")
    comparetext(f1name, f2name)
        
         

 
