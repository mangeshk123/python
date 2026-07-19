max = lambda no1, no2: no1 > no2 

def main():
    print("Enter FIRST number ")
    Num1 = int(input())
    print("Enter SECOND number ")
    Num2 = int(input())
    Ret = max(Num1,Num2)
    if Ret:
        print("Max is", Num1)
    else :
        print("Max is", Num2)

if __name__ == "__main__" :
    main()