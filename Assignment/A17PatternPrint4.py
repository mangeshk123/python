def printName(No):
    for i in range(No+1 , 1, -1):
        pattern = ""
        for j in range(1,i):
            pattern = pattern + "*      "
        print(pattern)

def main():
    print("Enter first number")
    Num = int(input())
    printName(Num)
    
if __name__ == "__main__" :
    main()