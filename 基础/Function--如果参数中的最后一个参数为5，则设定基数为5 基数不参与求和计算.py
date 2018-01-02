def he(*par):
    para = float(par)
    if para[len(para)-1] == 5:
        result = sum(para)-5
    else:
        result = sum(para)
    return result

data = input("请输入几个参数：")
he(data)
