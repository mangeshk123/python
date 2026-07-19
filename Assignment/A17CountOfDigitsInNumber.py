def countDigitsInNumber(No):
    Counter = 0
    while(No>0):
        No = int(No/10)
        Counter = Counter + 1
    return Counter
def main():
    print("Enter any number")
    Num = int(input())
    Ret = countDigitsInNumber(Num)
    print("Digits in Entered Number are : ",Ret)
        
if __name__ == "__main__" :
    main()