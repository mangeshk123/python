def main():
    max = 0
    num1 = int(input("Enter first Number : "))
    num2 = int(input("Enter second Number : "))
    if(num1 > num2):
        max = num1
    else:
        max = num2
    print(str(max)+ " is greater")

if __name__ == "__main__":
    main()