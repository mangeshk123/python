from functools import reduce

CheckEven= lambda No: (No % 2 == 0)
Increment= lambda No:(No + 1)
add = lambda No1,No2:No1 + No2


def main():
    Data = [13,12,8,10,11,20]
    print("Input data is",Data)
    FData = list(filter(CheckEven,Data))
    print("Input filtered data is",FData)
    MData = list(map(Increment,FData))
    print("Input Map data is",MData)
    Rdata = reduce(add,MData)
    print("Input Reduce data is",Rdata)

if __name__ == "__main__" :
    main()