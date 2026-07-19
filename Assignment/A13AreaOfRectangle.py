def area(l, b):
    return l * b

def main():
    print("Enter length of rectangle")
    l = int(input())
    print("Enter bredth of rectangle")
    b = int(input())

    print("Area of rectangle is : ", area(l,b))
    
if __name__ == "__main__" :
    main()