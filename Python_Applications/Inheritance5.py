class Base:
    def __init__(self):
        print("Inside Base constructer")
    
    def fun(self):
        print("Inside base fun()")

class Derived(Base):
    def sun(Self):
        print("Inside Derived fun()")

dobj = Derived()
dobj.fun()
dobj.sun()