import NumericOps
def main():
    print("please enter value1")
    V1 = int(input())
    print("please enter value2")
    V2 = int(input())
    Sum = NumericOps.sum(V1, V2)
    print("Sum is ", Sum)
if __name__ == "__main__" :
    main()