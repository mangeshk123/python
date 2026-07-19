def countOfDigits(No):
    counter = 0
    while No > 0:
        No = int(No / 10)
        counter = counter + 1
    return counter
        
def main():
    print("Enter any number")
    No = int(input())
    Ret = countOfDigits(No)
    print("Count of digits is", Ret)
    
if __name__ == "__main__" :
    main()