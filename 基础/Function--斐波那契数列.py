while True:
    def fibonacci(m):
        a = 0
        b = 1
        c = 1
        n = int(m)-2
        print(a, b, end =" ")
        
        while n > 0:
            c = a + b
            print (c, end = " ")
            a = b
            b = c
            n = n-1
            

    m = input ("请输入斐波那契出现的次数：")
    fibonacci(m)
    print ("\n")
        
