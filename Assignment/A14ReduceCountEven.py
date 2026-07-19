from functools import reduce
even = lambda num :num%2 == 0

sum = lambda a,b :a if a > b else b

def main():
    Numbers = [2,6,4,9,7]
    fData = list(filter(even,Numbers))
    print(len(fData))

if __name__ == "__main__" :
    main()