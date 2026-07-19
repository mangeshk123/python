def Sum(No1, No2):
    return No1 + No2

def main():
    print("Enter First number ")
    Num1 = int(input())
    print("Enter First number ")
    Num2 = int(input())
    Ret = Sum(Num1,Num2)
    print("Sum = ",Ret)
    
if __name__ == "__main__" :
    main()