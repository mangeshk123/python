def sequence(No):
    Sequence = []
    for i in range(1, No+1):
        Sequence.append(i)
    return Sequence

def main():
    print("Enter any number")
    Num = int(input())

    Ret = sequence(Num)
    print(Ret)

if __name__ == "__main__" :
    main()