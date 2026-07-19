
def main():
    print("Enter number ")
    cube = lambda no: no * no * no
    Num = int(input())
    Ret = cube(Num)
    print("cube is", Ret)

if __name__ == "__main__" :
    main()