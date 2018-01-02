while True:
    def fibonacci(x):
        if x == 1:
            return 0
        elif x == 2:
            return 1
        elif x >= 2:
            return (fibonacci(x-1) + fibonacci (x-2))

    number = int(input("请输入斐波那契出现的次数："))
    for i in range(number):
        print(fibonacci(i+1),end = " ")

    print("\n")
