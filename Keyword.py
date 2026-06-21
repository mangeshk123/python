def Area(Radius,Pi):
    Ans = Pi * Radius * Radius
    return Ans

def main():
    Ret = Area(Pi=3.14, Radius = 10.5)
    print("Area of circle is :", Ret)
    
if __name__ == "__main__":
    main()