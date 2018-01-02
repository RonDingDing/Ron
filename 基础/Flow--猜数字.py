import random
secret = random.randint(1,10)
temp = input("猜猜我在想哪个数字：")
guess = int(temp)
cishu = 1
while guess != secret and cishu < 3:
    temp = input("猜错啦，重新输入吧：")
    guess = int(temp)
    if guess == secret:
        print ("猜中了。")
    else:
        if guess > secret:
            print ("大了大了")
        else:
            print ("小了小了")
    cishu = cishu + 1
print("猜中了，结束了。")
