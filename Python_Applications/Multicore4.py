import os
import time
import multiprocessing

def sumcube(no):
    sum = 0
    print("Process is running with pid ", os.getpid())
    for i in range(1,no+1):
        sum = sum + (i**3)
    return sum

def main():
    arr = [10000000,20000000,30000000,40000000,50000000]
    res = []
    start_time = time.perf_counter()
    pobj = multiprocessing.Pool()
    
    res = pobj.map(sumcube,arr)
    pobj.close()
    pobj.join

    end_time = time.perf_counter()
    print(res)
    print(f"Time taken is {end_time - start_time:4f}")
    
if __name__ == "__main__":
    main()
