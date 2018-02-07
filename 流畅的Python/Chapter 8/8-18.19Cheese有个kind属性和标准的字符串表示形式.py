class Cheese:
    def __init__(self, kind):
        self.kind = kind

    def __repr__(self):
        return "Cheese(%r)" % self.kind


import weakref

stock = weakref.WeakValueDictionary()
catalog = [Cheese("Red Leicester"), Cheese("Tilsit"), Cheese("Brie"), Cheese("Parmesan")]
for cheese in catalog:
    stock[cheese.kind] = cheese

print(sorted(stock.keys()))
del catalog
print(sorted(stock.keys()))
del cheese
print(sorted(stock.keys()))
# 删除catalog之后，对各种Cheese("Red Leicester"), Cheese("Tilsit"), Cheese("Brie")的引用都没有了，stock把这些都删除，但是还有
# cheese，它一直指向Cheese("Parmesan")