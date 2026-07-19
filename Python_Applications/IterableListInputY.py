def main():
    Marks = list()
    print("Enter Number of students :")
    noOfStudents = int(input())
    for counter in range(noOfStudents):
        print("Input number :",counter)
        no = int(input())
        Marks.append(no)
    print("List is",Marks)

if __name__ == "__main__":
    main()
    