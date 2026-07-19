from abc import ABC, abstractmethod
class Demo(ABC):
    def __init__(self, A):
        self.No = A
    def __add__(self, other):
        return self.No + other.No
    def __sub__(self, other):
        return self.No - other.No
    def __mul__(self, other):
        return self.No * other.No
    def __truediv__(self, other):
        return self.No / other.No
dobject1 = Demo(11)
dobject2 = Demo(21)

print("Sum : ",dobject1 + dobject2)  #Obj1.__add__(Obj2) -> __add__(Obj1,Obj2)
print("Sub : ",dobject1 - dobject2)  #Obj1.__add__(Obj2) -> __sub__(Obj1,Obj2)
print("Multi : ",dobject1 * dobject2) #Obj1.__add__(Obj2) -> __mul__(Obj1,Obj2)
print("Div : ",dobject1 / dobject2)  #Obj1.__add__(Obj2) -> __truediv__(Obj1,Obj2)
