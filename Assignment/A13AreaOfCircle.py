def area(radius):
    pi = 3.14
    return pi * radius**2

def main():
    print("Enter length of circle")
    radius = int(input())

    print("Area of circle is : ", area(radius))
    
if __name__ == "__main__" :
    main()