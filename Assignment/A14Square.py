
def main():
    print("Enter number ")
    square = lambda no: no * no
    Num = int(input())
    Ret = square(Num)
    print("Square is", Ret)

if __name__ == "__main__" :
    main()