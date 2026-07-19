from functools import reduce
maximum = lambda a,b :a if a > b else b

def main():
    Numbers = [2,6,4,9,7]
    mData = reduce(maximum,Numbers)
    print(mData)

if __name__ == "__main__" :
    main()