# Define lambda to return the larger of two numbers
maximum = lambda no1, no2: no1 if no1 > no2 else no2

def main():
    print("Enter FIRST number ")
    Num1 = int(input())
    print("Enter SECOND number ")
    Num2 = int(input())
    
    # Use lambda to get max
    Ret = maximum(Num1, Num2)
    print("Max is", Ret)

if __name__ == "__main__":
    main()
