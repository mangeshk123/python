def getStatus(No):
    if No >= 75:
        print("Distinction")
    elif No < 75 and No >= 60:
        print("First class")
    elif No < 60 and No >= 50:
        print("Second class")
    else :
        print("Failed")


def main():
    print("Enter percentage ")
    Num = int(input())
    Ret = getStatus(Num)

if __name__ == "__main__" :
    main()