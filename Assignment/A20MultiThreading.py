import threading
def evenNumbers(No):
    for i in range(1,No):
        if(i%2 == 0):
            print(i)

def oddNumbers(No):
    for i in range(1,No):
        if(i%2 == 1):
            print(i)

def main():
    tobj1 =threading.Thread(target=evenNumbers, args = (20,))
    tobj2 =threading.Thread(target=oddNumbers, args = (20,))
    tobj1.start()
    tobj2.start()
if __name__ == "__main__":
    main()