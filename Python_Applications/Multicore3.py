import os
import time
def sumcube(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum + (i**3)
    return sum

def main():
    arr = [10000000,20000000,30000000,40000000,50000000]
    res = []
    start_time = time.perf_counter()
    for value in arr:
        res.append(sumcube(value))
    end_time = time.perf_counter()
    print(res)
    print(f"Time taken is {end_time - start_time:4f}")
    
if __name__ == "__main__":
    main()
