def main():
    Marks = [11,21,51,101]
    print("Sum of Data fromlist is :")
    Sum = 0
    for no in Marks:
        print(no)
        Sum = Sum + no
    print("Sum is :", Sum)
    print("-"*40)
    Marks[2] = 59
    Sum = 0
    for no in Marks:
        print(no)
        Sum = Sum + no
    print("Sum is :", Sum)

if __name__ == "__main__":
    main()
    