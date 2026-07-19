def findFactors(No):
    Factors = []
    for i in range(1, No+1):
        if(No % i == 0):
            Factors.append(i)
    return Factors

def main():
    print("Enter any number")
    Num = int(input())

    Ret = findFactors(Num)
    print(Ret)

if __name__ == "__main__" :
    main()