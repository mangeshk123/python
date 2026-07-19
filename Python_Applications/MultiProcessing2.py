import multiprocessing
import time
import os
# 2+4+6+8
def sumeven(No):
    print(f"PID of sumeven process is {os.getpid()} , ppid is {os.getppid()}" )
    sum  = 0
    for i in range(2,No,2):
        sum = sum + i
    print(f"Sum even is {sum}")

# 1+3+5+7+9
def sumodd(No):
    print(f"PID of sumodd process is {os.getpid()} , ppid is {os.getppid()}" )
    sum  = 0
    for i in range(1,No,2):
        sum = sum + i
    print(f"Sum odd is {sum}")

def main():
    print(f"PID of main process is {os.getpid()} , ppid is {os.getppid()}" )
    start_time = time.perf_counter()
    t1 = multiprocessing.Process(target=sumeven, args=(100,))
    t2 = multiprocessing.Process(target=sumodd, args=(100,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()
    print(f"Time required is : {end_time - start_time:4f} ")

if __name__ == "__main__":
    main()