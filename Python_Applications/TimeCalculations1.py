# 6: 1*2*3*4*5*6
def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact* i
    return fact

def main():
    value = int(input("Enter number : "))
    ret = factorial(value)
    print("Factorial is",ret)

if __name__ == "__main__":
    main()
