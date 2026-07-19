even = lambda no: no % 2 ==0 

def main():
    print("Enter number ")
    No = int(input())
    Ret = even(No)
    if Ret:
        print("Number is even")
    else :
        print("Number is not even")

if __name__ == "__main__" :
    main()