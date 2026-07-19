from functools import reduce

def countOccurences(search, List):
    count = 0
    for num in List:
        if num == search :
            print(num)
            count = count + 1
    return count

def main():
    Arr = []
    print("Enter how many number you want to enter :")
    Num = int(input())
    for i in range(Num):
        print("Enter number you want to add :")
        member = int(input())
        Arr.append(member)
    print("Enter hnumber you want to search :")
    search = int(input())
    Ret = countOccurences(search,Arr)
    print("Occurences for searched Numbers are : ",Ret)
        
if __name__ == "__main__" :
    main()
    