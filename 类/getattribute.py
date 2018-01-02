class C:
    def __getattribute__(self, name):
        print("getattribute")
        return super().__getattribute__(name)
    
    def __getattr__(self,name):
        print("getattr")
	
    def __setattr__(self,name,value):
        print("setattr")

    def __delattr__(self, name):
        print("delattr")
        super().__delattr__(name)
