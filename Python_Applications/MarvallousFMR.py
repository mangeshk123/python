CheckEven= lambda No: (No % 2 == 0)
Increment= lambda No:(No + 1)
add = lambda No1,No2:No1 + No2

def filterX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no) # CheckEven(no)
        if(Ret == True):
            Result.append(no)
    return Result

def mapX(Task, Elements):
    Result = list()
    for no in Elements:
        Ret = Task(no) # CheckEven(no)
        Result.append(Ret)
    return Result

def reduceX(Task, Elements):
    Result = list()
    Sum = 0
    for no in Elements:
        Sum = Task(Sum,no) # add(no)        
    return Sum


def main():
    Data = [13,12,8,10,11,20]
    print("Input data is",Data)
    FData = list(filterX(CheckEven,Data))
    print("Input filtered data is",FData)
    MData = list(mapX(Increment,FData))
    print("Input Map data is",MData)
    Rdata = reduceX(add,MData)
    print("Input Reduce data is",Rdata)

if __name__ == "__main__" :
    main()