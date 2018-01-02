password = input("请输入你的密码： ")
number = "1234567890"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = r"""`!@#$%^&*()_+-=/{}[]\|"';:/?,.<>"""

length = len(password)
while True:
    while password.isspace() or length == 0:
        password = input("你输入的密码为空，请重新输入： ")

    if length <= 8:
        miao = 1
    elif 8 < length < 16:
        miao = 2
    elif 16 <= length:
        miao = 3

    diao = 0

    for each in password:
        if each in symbols:
            miao = miao + 1
            break

    for each in password:
        if each in chars:
            miao = miao + 1
            break

    for each in password:
        if each in number:
            miao = miao + 1
            break

    while 1:
        print ("您的密码安全级别评定为：", end = " ")
        if miao or diao == 1:
            print ("低")
            print ("请按以下方式提升你的密码安全级别：\n \t1.密码必须由数字、字母及特殊字符三种组合\n\
    \t2.密码只能由字母开头\n\
    \t3.密码长度不低于16位")
        elif miao or diao == 2:
            print ("中")
            print ("请按以下方式提升你的密码安全级别：\n \t1.密码必须由数字、字母及特殊字符三种组合\n\
    \t2.密码只能由字母开头\n\
    \t3.密码长度不低于16位")
        elif miao or diao == 3:
            print ("高")
            print ("密码很安全")
        break
    break

input()
