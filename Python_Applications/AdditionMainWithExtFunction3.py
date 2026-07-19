from NumericOps import sum,substract
def main():
    print("please enter value1")
    V1 = int(input())
    print("please enter value2")
    V2 = int(input())
    Sum = sum(V1, V2)
    print("Sum is ", Sum)
    SubStr = substract(V1, V2)
    print("Substraction is ", SubStr)
if __name__ == "__main__" :
    main()