from functools import reduce
FilterBetween70and90 = lambda no: no >= 70 and no <= 90
MapAdd10 = lambda no: no+10
ReduceProduct = lambda no1,no2:no1*no2
def main():
    Arr = [4,8,7,55,67,78,43,88,87,96]
    fData = list(filter(FilterBetween70and90, Arr))
    print(fData)
    mData = list(map(MapAdd10,fData))
    print(mData)
    output = reduce(ReduceProduct,mData)
    print(output)


if __name__ == "__main__":
    main()