# Accept: Multiple parameter
# Return: Multiple value
from NumericOps import sum, substract
def calculate(Value1, Value2):
    print("Inside calculate")
    return sum(Value1,Value2),substract(Value1,Value2)

def main():
    V1 = int(input("Enter First number : "))
    V2 = int(input("Enter Second number: "))
    Add,Sub = calculate(V1,V2)
    print("add",Add)
    print("sub",Sub)
    
if __name__ == "__main__" :
    main()