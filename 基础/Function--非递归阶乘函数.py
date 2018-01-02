while True:
    def factorial(n):
        result = n
        for i in range(1,n):
            result =i*result
        return result

    number = int(input("请输入一个正整数："))
    re = factorial(number)
    print("%d的阶乘是：%d" %(number, re))
