def square(No):
    return No * No
def main():
    Numbers = [2,6,4,9,7]
    mData = list(map(square,Numbers))
    print(mData)

if __name__ == "__main__" :
    main()