def printName(No):
    for i in  range(No):
        pattern = ""
        for j in range(No):
            pattern = pattern + "* "
        print(pattern)

def main():
    print("Enter first number")
    Num = int(input())
    printName(Num)
    
if __name__ == "__main__" :
    main()