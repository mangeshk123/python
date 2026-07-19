class Demo:
    def __init__(self):
        print("inside constructer")
    def __del__(self):
        print("inside destructer")

obj1 = Demo()
obj2 = Demo()

print("End of app")