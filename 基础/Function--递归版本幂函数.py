while True:
    def power(k,u):
        g = 0
        y = int(u)
        x = int(k)
        m = 1
        if y == -1:
            g = 1/x
        if y == 0:
            g = 1
        elif y == 1:
            g = x
        elif y > 0:
            g = x * power(x,(y-1))
        elif y < 0:
            g = (1/x) * power(x,(y+1))
            
        return g

    ada = input("请输入整数1:")
    bdb = input("请输入整数2:")
    print (power(ada,bdb))
        
