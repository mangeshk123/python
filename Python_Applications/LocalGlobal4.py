No = 11 # Global var
def Display():
    global No
    No = 21
    print("from Display",No)
print("Before :",No)
Display()
print("After :",No)