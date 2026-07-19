from functools import reduce
divBy5and3 = lambda no :no %3 ==0 and no%5 ==0

def main():
    Numbers = [2,15,4,9,30]
    mData = list(filter(divBy5and3, Numbers))
    print(mData)

if __name__ == "__main__" :
    main()