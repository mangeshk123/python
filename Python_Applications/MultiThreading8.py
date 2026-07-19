import threading
import time
# 2+4+6+8
def sumeven(No):
    print("TID of SumEven is : ", threading.get_ident())


# 1+3+5+7+9
def sumodd(No):
        print("TID of SumOdd is : ", threading.get_ident())

def main():
    print("TID of main thread is : ", threading.get_ident())
    start_time = time.perf_counter()
    t1 = threading.Thread(target=sumeven, args=(100000000,))
    t2 = threading.Thread(target=sumodd, args=(100000000,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    end_time = time.perf_counter()
    print(f"Time required is : {end_time - start_time:4f} ")

if __name__ == "__main__":
    main()