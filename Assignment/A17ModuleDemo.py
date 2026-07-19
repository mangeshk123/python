import MathUtil as mu
def main():
    print("Enter first number")
    Num1 = int(input())
    print("Enter second number")
    Num2 = int(input())
    Sum = mu.add(Num1,Num2)
    Sub = mu.sub(Num1,Num2)
    print("Sum is ",Sum)
    print("Sub is ",Sub)

if __name__ == "__main__" :
    main()