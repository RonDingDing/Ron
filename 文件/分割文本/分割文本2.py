

def save_file(xiaotugou,xiaohei,count):
    file_name_xiaotugou = "boy_" + str(count) + ".txt"
    file_name_xiaohei = "girl_" + str(count) + ".txt"

    boy_file = open(file_name_xiaotugou, "w")
    girl_file = open(file_name_xiaohei, "w")
        

    boy_file.writelines(xiaotugou)
    girl_file.writelines(xiaohei)
        
    boy_file.close()
    girl_file.close()
        
        
    

def split_file(file_name):
    xiaotugou = []
    xiaohei = []
    count = 1
    
    f = open("record.txt","r")

    for each_line in f:
        if each_line[:6] != "======":
            (role, line_spoken) = each_line.split("：",1)
            if role == "小土狗":
                xiaotugou.append(line_spoken)
            if role == "小黑":
                xiaohei.append(line_spoken)
        else:
            save_file(xiaotugou, xiaohei, count)
            
            count = count + 1
            xiaotugou = []
            xiaohei = []

    save_file(xiaotugou, xiaohei, count)

    f.close()

    
split_file("record.txt")


