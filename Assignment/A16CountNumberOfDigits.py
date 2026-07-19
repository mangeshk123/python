def countNumberOdDigits(opString):
    Counter = 0
    for i in range(1,len(opString)+1):
        Counter = Counter + 1
    print(Counter)
    
def main():
    print("Enter any Text")
    Num = input()
    countNumberOdDigits(Num)
if __name__ == "__main__" :
    main()