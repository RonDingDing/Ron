def ds():
    file_name_origin = input("请输入文件名：")
    file_name = file_name_origin + ".txt"
    facebook = []
    content = input("请输入内容【单独输入':w'保存退出】：") + "\n"
    file = open(file_name, "w")

    while content != ":w\n":
        facebook.append(content)
        content = ""
        content = input("请继续输入：") + "\n"

    file.writelines(facebook)
    file.close()


while True:
    print("\n")
    ds()
