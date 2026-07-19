def isPrimeNumber(No):
    flag = False
    for i in range(2,No):
        if(No % i == 0):
            flag  = True
    return flag
def main():
    print("Enter any number")
    No = int(input())
    Ret = isPrimeNumber(No)
    if(Ret):
        print("Entered number is not prime")
    else:
        print("Entered number is prime")
if __name__ == "__main__" :
    main()