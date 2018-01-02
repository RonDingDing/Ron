import math
class Point:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getXY(self):
        return (self.x, self.y)


class Straightline():
    def __init__(self, p1, p2):
        self.a = p1.getX() - p2.getX()
        self.b = p1.getY() - p2.getY()
        self.len = math.sqrt(self.a*self.a + self.b*self.b)

    def getLen(self):
        return self.len        
        
    
