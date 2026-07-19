class Base:
    def __init__(self):
        print("Inside Base constructer")

class Derived(Base):
    def __init__(self):
        super().__init__()
        print("Inside Derived constructer")

dobj = Derived()