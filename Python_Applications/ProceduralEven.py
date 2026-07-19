def CheckEven(no):
    if (no % 2 == 0):
        print("It's Even number")
    else:
        print("It's Odd number")

def main():
    value = int(input("Enter number :"))
    CheckEven(value)

if __name__=="__main__":
    main()