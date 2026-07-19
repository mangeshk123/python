
even = lambda no : no % 2 == 0

def main():
    Numbers = [2,6,4,9,7]
    mData = list(filter(even,Numbers))
    print(mData)

if __name__ == "__main__" :
    main()