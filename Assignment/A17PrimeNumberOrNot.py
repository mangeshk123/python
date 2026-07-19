def isPrimeNumber(No):
    flag = 0
    for i in range(2,No):
        if(No % i == 0):
            flag = 1
    return True if flag == 0 else False

def main():
    print("Enter any number")
    Num = int(input())
    Ret = isPrimeNumber(Num)
    if(Ret):
        print("Entered Number is prime")
    else:
        print("Entered Number is not prime")
    
if __name__ == "__main__" :
    main()