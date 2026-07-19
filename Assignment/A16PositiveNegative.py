def signCheck(No):
    if No > 0:
        print("Number is positive")
    elif No < 0:
        print("Number is negative")
    else:
        print("Zero")

def main():
    print("Enter any number")
    Num = int(input())
    signCheck(Num)
    
if __name__ == "__main__" :
    main()