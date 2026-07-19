def sumOfDigits(No):
    Sum = 0
    while No > 0:
        Rem = No % 10
        No = int(No / 10)        
        Sum = Sum + Rem

    if Sum < 10 :
        return Sum
    else:
        return sumOfDigits(Sum)
def main():
    print("Enter any number")
    No = int(input())
    Ret = sumOfDigits(No)
    print(Ret)
    
if __name__ == "__main__" :
    main()