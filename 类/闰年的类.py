class Fibs:
        def __init__(self, year, n=2016):
                self.year = year
                self.n = n

        def __iter__(self):
                return self

        def __next__(self):
                self.year +=1
                if self.year > self.n:
                        raise StopIteration
                elif (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0):                          
                        return self.year


fibs = Fibs()
for each in fibs:
        print (each)
