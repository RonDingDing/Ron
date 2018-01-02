##整体思路：先确定主程序，然后再去写每一个函数##


import urllib.request
import os
 
def open_url(url):                                  #打开url地址
    req = urllib.request.Request(url)
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 BIDUBrowser/7.6 Safari/537.36")
    #加上header的User-Agent来蒙骗网站
    response = urllib.request.urlopen(url)
    html = response.read()
    return html
    
def find_imgs_address(url):                         #在url地址上寻找图片的地址，传入img_addrs
    html = open_url(url).decode("utf-8")            #调用open_url解码
    img_addrs = []

    a = html.find("img src=")                       #寻找img scr=也就是jpg文件之前

    while a!=-1:                                    #找到会返回index，找不到会返回-1，这里是找到就继续找下去的意思
        b = html.find(".jpg", a, a+255)             #b是.jpg后面的index，从a开始，到a+255寻找
        c = html.find("_s", a, a+255)
        if b !=-1 and c==-1:                        #c其实是研究文件名后发现_s都是小图，不想要。如果b找到，就把图片地址加入img_addrs列表。a+9是img src=，b+4是.jpg 
            img_addrs.append(html[a+9:b+4])
        else:                                       #如果找不到，b要移位，就是从上一次找到img src=之后开始找
            b = a+9
        a = html.find("img src=", b)                #然后从b开始找img src=

    return img_addrs                                #返回img_addrs
        

def save_imgs(img_addrs): 
     
    for each in img_addrs:                                   #打开img_addrs列表，迭代
         
        filename = each.split("/")[-1] + each.split("/")[-2] + each.split("/")[-3] +".jpg"   #改变文件的名字而已
        
        
        with open(filename, "wb") as f:                      
            img = open_url(each)
            f.write(img)                                     #保存


            
###以下是主程序##
def download_mm(folder="ooxx"):
    os.mkdir(folder)                        #创建一个文件夹，默认是ooxx
    os.chdir(folder)                        #将当前文件夹变换到ooxx

    i = 0 
    while True:                             #这一部分是研究了http://www.mmjpg.com/得出的结果，后面加上mm/，然后是三位数字，这样可以打开每一个页面
        i+=1
        print("i=",i)
        if i >=999:
            break
        
        count = "%03d" % i
        url = "http://www.mmjpg.com/mm/" + str(count)     
        print(url)                          #打印当前访问的地址url
        open_url(url)                       #打开url地址                     
        img_addrs = find_imgs_address(url)  #在url地址上寻找图片的地址，传入img_addrs
        save_imgs(img_addrs)                #将img_addrs存为图片

        j = 0
        while True:
            j+=1
            
            if i >=999:
                break
            url2 = url + "/" + str(j)                
            try:
                print(url2)
                open_url(url2)
                img_addrs2 = find_imgs_address(url2)   
                save_imgs(img_addrs2)
            except:
                print("出错了")
                                    
                break
 
        
        
        
         
 

if __name__ == "__main__":
    download_mm()
     
    
    
