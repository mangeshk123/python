class Demo:
    # Class variable
    Value1 = 10
    Value2 = 20

    def __init__(self):
        self.No1 = 11
        self.No2 = 22
    
    # instance method
    def fun(self):
        print("Inside instance method fun()")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)

dObj = Demo()
dObj.fun()