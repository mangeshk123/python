def sumoffactorial(No):
    Sum = 0
    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i
    return Sum

def main():
    print("Enter any number")
    Num = int(input())
    Ret = sumoffactorial(Num)
    print("Sum of Factors is :", Ret)
    
if __name__ == "__main__" :
    main()