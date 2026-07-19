import time
def factorial(no):
    fact = 1
    for i in range(1,no+1):
        fact = fact* i
    return fact

def main():
    start = time.perf_counter()
    value = int(input("Enter number : "))
    ret = factorial(value)
    end = time.perf_counter()
    print(f"Factorial of {value} is {ret}")
    print(f"time spent {end - start : .5f} seconds")

if __name__ == "__main__":
    main()
