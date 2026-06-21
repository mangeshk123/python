# Accept: Multiple parameter
# Return: Multiple value
def add(Value1, Value2):
    print("Inside add")
    ret1 = Value1+Value2
    ret2 = Value1*Value2
    return ret1, ret2

def main():
    ret1,ret2 = add(10,20)
    print("add",ret1)
    print("multiply",ret2)

if __name__ == "__main__" :
    main()