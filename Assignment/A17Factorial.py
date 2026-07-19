def factorial(No):
    factorial = 1
    for i in range(1,No +1):
        factorial = factorial * i
    return factorial

def main():
    print("Enter any number")
    Num = int(input())
    Ret = factorial(Num)
    print("Factorial is :", Ret)
    
if __name__ == "__main__" :
    main()