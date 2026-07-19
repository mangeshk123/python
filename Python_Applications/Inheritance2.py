class Base:
    def __init__(self):
        print("Inside Base constructer")

class Derived(Base):
    def __init__(self):
        print("Inside Derived constructer")

bobj = Base()