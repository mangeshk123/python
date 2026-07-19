class Base1:
    def fun(self):
        print("Inside base1 fun()")

class Base2:
    def gun(self):
        print("Inside base2 gun()")

class Derived(Base1,Base2):
    def sun(Self):
        print("Inside Derived fun()")

dobj = Derived()
dobj.fun()
dobj.sun()
dobj.gun()