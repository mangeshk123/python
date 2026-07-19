class Base:
    def __init__(self):
        print("Inside Base constructer")
    
    def fun(self):
        print("Inside base fun()")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived constructer")

dobj = Derived()
dobj.fun()