even = lambda no: no % 5 == 0 

def main():
    print("Enter number ")
    No = int(input())
    Ret = even(No)
    if Ret:
        print("Number is Divisable by 5")
    else :
        print("Number is not Divisable by 5")

if __name__ == "__main__" :
    main()