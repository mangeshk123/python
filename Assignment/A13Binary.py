def getBinary(No):
    Sum = ""
    while No > 0:
        Rem = No % 2
        No = int(No / 2)
        Sum = Sum + str(Rem)   
    return reverseString(Sum)

def reverseString(text):
    reversedText =""# 13 --- 1101
    for i in range(len(text)-1,-1,-1):
        reversedText = reversedText + text[i]
    return reversedText

def main():
    print("Enter any number")
    Num = int(input())

    Ret = getBinary(Num)
    print(Ret)

if __name__ == "__main__" :
    main()