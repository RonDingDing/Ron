class Rectangle:
    length = 5  #这里其实用__init__方法定义会更加准确
    width = 4
    
    def setRect(self):
        print("请输入矩形的长和宽...")
        self.length = float(input('长：'))
        self.width = float(input('宽：'))
        if self.length < self.width:
            huan = self.length
            self.length = self.width
            self.width = huan
            

    def getRect(self):
        print('这个矩形的长是：%.2f，宽是：%.2f' % (self.length, self.width))
        
    def getArea(self):
        return self.length * self.width
