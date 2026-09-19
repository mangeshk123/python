import threading
def evenNumbers(No):
    Sum = 0    
    for i in range(1,No):
        if(i%2 == 0):
            Sum = Sum + i
    print("even =",Sum)

def oddNumbers(No):
    Sum = 0    
    for i in range(1,No):
        if(i%2 == 1):
            Sum = Sum + i
    print("odd=",Sum)

def main():
    tobj1 =threading.Thread(target=evenNumbers, args = (10,))
    tobj2 =threading.Thread(target=oddNumbers, args = (10,))
    tobj1.start()
    tobj2.start()
if __name__ == "__main__":
    main()