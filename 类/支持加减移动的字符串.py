class Nstr(str):
        def __init__(self, arg = ""):
                if isinstance (arg, str):
                        self.total = 0
                        for each in arg:
                                self.total += ord(each)
                else:
                        print("参数错误！")
        def __lshift__(self, other):
                return self[other:] + self[:other]
        
        def __rshift__(self, other):
                return self[:-other] + self[-other:]
      
        def __sub__(self, other):
                return self.replace(other, "")

        def __add__(self, other):
                return self.total + other.total

        def __mul__(self, other):
                return self.total * other.total
        
        def __trudiv__(self, other):
                return self.total / other.total

        def __floordiv__(self, other):
                return self.total // other.total  
