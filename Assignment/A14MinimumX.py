max = lambda no1, no2: no1 if no1 < no2 else no2 

def main():
    print("Enter FIRST number ")
    Num1 = int(input())
    print("Enter SECOND number ")
    Num2 = int(input())
    Ret = max(Num1,Num2)
    if Ret:
        print("Min is", Num1)
    else :
        print("Min is", Num2)

if __name__ == "__main__" :
    main()