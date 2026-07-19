def printName(No):
    for i in range(1,No+1):
        pattern = ""
        for j in range(1,i+1):
            pattern = pattern + f"{j} "
        print(pattern)

def main():
    print("Enter first number")
    Num = int(input())
    printName(Num)
    
if __name__ == "__main__" :
    main()