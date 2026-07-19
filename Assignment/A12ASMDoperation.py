def add(No1, No2):
    return No1 + No2
def substract(No1, No2):
    return No1 - No2
def multiply(No1, No2):
    return No1 * No2
def divide(No1, No2):
    return No1 / No2
def main():
    print("Enter first number")
    Num1 = int(input())
    print("Enter second number")
    Num2 = int(input())

    print("Addition is : ", add(Num1,Num2))
    print("Substraction is : ", substract(Num1,Num2))
    print("Multiplication is : ", multiply(Num1,Num2))
    print("Division is : ", divide(Num1,Num2))

if __name__ == "__main__" :
    main()