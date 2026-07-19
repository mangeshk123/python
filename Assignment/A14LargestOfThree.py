maxNumber = lambda no1,no2,no3: max(no1,no2,no3) 

def main():
    print("Enter first number ")
    N1 = int(input())
    print("Enter Second number ")
    N2 = int(input())
    print("Enter Third number ")
    N3 = int(input())
    Ret = maxNumber(N1, N2, N3)
    print("Sum is ", Ret)

if __name__ == "__main__" :
    main()