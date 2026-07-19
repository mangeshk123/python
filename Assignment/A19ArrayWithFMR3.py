from functools import reduce
def FilterPrime(No):    
    for i in range(2,int(No/2)): 
        if(No % i == 0):
            return True
    return False

MapAdd10 = lambda no: no*2

ReduceProduct = lambda no1,no2:no1 if no1>no2 else no2

def main():
    Arr = [4,8,7,55,67,78,43,88,87,96]
    fData = list(filter(FilterPrime, Arr))
    print(fData)
    mData = list(map(MapAdd10,fData))
    print(mData)
    output = reduce(ReduceProduct,mData)
    print(output)


if __name__ == "__main__":
    main()