sum = lambda no1,no2: no1 + no2 

def main():
    print("Enter number ")
    N1 = int(input())
    print("Enter number ")
    N2 = int(input())
    Ret = sum(N1, N2)
    print("Sum is ", Ret)

if __name__ == "__main__" :
    main()