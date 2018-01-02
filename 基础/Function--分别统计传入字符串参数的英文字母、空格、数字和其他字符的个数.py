def shushu(*param):
    length = len(param)
    for i in range(length):
        letters = 0
        space = 0
        digit = 0
        others = 0

        for each in param[i]:
            if each.isdigit():
                digit += 1
            elif each.isalpha:
                letters += 1
            elif each == " ":
                space += 1
            else:
                others += 1
        print("第 %d 个字符串共有：英文字母 %d 个，数字 %d 个，空格 %d 个，其他字符 %d 个。"% (i+1, letters, digit, space, others))
