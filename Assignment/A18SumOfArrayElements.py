from functools import reduce

def sumtDigitsInNumber(No1,No2):
    return No1 + No2

def main():
    Arr = []
    print("Enter how many number you want to enter :")
    Num = int(input())
    for i in range(Num):
        print("Enter number you want to add :")
        member = int(input())
        Arr.append(member)
    Ret = reduce(sumtDigitsInNumber,Arr)
    print("Sum of Digits in Entered Number are : ",Ret)
        
if __name__ == "__main__" :
    main()
    