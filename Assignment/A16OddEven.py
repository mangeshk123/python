def oddOrEven(No):
    if(No%2 == 0):
        print("Entered number is even")
    else:
        print("Entered number is Odd")

def main():
    print("Enter number ")
    Num = int(input())
    oddOrEven(Num)
    
if __name__ == "__main__" :
    main()