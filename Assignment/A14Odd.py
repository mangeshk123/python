even = lambda no: no % 2 == 1 

def main():
    print("Enter number ")
    No = int(input())
    Ret = even(No)
    if Ret:
        print("Number is Odd")
    else :
        print("Number is not Odd")

if __name__ == "__main__" :
    main()