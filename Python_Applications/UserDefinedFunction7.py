# Accept: Multiple parameter
# Return: Multiple value
def calculate(Value1, Value2):
    print("Inside add")
    Add = Value1+Value2
    Mult = Value1*Value2
    Div = Value1/Value2
    Sub = Value1 - Value2
    return Add, Mult, Div, Sub

def main():
    V1 = int(input("Enter First number : "))
    V2 = int(input("Enter Second number: "))
    Add,Mult,Div,Sub = calculate(V1,V2)
    print("add",Add)
    print("multiply",Mult)
    print("sub",Sub)
    print("divison",Div)

if __name__ == "__main__" :
    main()