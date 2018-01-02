def suishu(x):
    if x == 1:
        return 10
    if x > 1:
        return suishu(x-1) + 2

while True:          

    m = int(input("请输入这是第几个人："))
    
  
    for i in range(1,m+1):
        print(suishu(i), end = " ")
    print("\n")
        

        
