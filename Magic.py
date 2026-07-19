from abc import ABC, abstractmethod
class Demo(ABC):
    def __init__(self, A):
        self.No = A
   
dobject1 = Demo(11)
dobject2 = Demo(21)

print("Sum : ",dobject1 + dobject2) #Error
