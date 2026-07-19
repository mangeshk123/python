def Sum(Marks):
    Sum = 0
    for no in Marks:
        Sum = Sum+ no
    return Sum

def main():
    Marks = list()
    print("Enter Number of students :")
    noOfStudents = int(input())
    for counter in range(noOfStudents):
        print("Input number :",counter)
        no = int(input())
        Marks.append(no)
    print("Summation is : ", Sum(Marks))

if __name__ == "__main__":
    main()
    