No = 11 # Global var
def Display():
    print("From Display value of a is :",a) #Error
    print("From Display :",No)
def Demo():
     a = 23 #Local
     print("From Demo value of a is :",a)
     print("From Demo :",No)

Demo()
Display()