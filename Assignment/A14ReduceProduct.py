from functools import reduce
Sum = lambda sum,no : sum * no

def main():
    Numbers = [2,6,4,9,7]
    mData = reduce(Sum, Numbers)
    print(mData)

if __name__ == "__main__" :
    main()