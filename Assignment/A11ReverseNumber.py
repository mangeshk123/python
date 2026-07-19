def ReverseOfDigits(No):
    Rem = 0
    ReversedNo = 0
    while No > 0:
        Rem = No % 10
        ReversedNo = ReversedNo * 10 + Rem 
        No = int(No / 10)
        
    return ReversedNo
        
def main():
    print("Enter any number")
    No = int(input())
    Ret = ReverseOfDigits(No)
    print("Reversal of digits is", Ret)
    
if __name__ == "__main__" :
    main()