def isPerfect(No):
    Sum = 0
    for i in range(1, No):
        if(No % i == 0):
            Sum = Sum + i
    print(Sum)
    return Sum == No

def main():
    print("Enter any number")
    Num = int(input())

    Ret = isPerfect(Num)
    if Ret:
        print("Entered Number is perfect")
    else:
        print("Entered Number is not perfect")

if __name__ == "__main__" :
    main()