def sumtDigitsInNumber(No):
    Sum = 0
    while(No>0):
        Rem = No % 10
        No = int(No/10)
        Sum = Sum + Rem
    return Sum

def main():
    print("Enter any number")
    Num = int(input())
    Ret = sumtDigitsInNumber(Num)
    print("Sum of Digits in Entered Number are : ",Ret)
        
if __name__ == "__main__" :
    main()