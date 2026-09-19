import threading
def evenNumbers(No):
    factors =[]    
    for i in range(1,(No//2 +1)):
        if(No%i == 0 and i%2 == 0):
            factors.append(i)
    print(factors)
def oddNumbers(No):
    factors =[]    
    for i in range(1,(No//2 +1)):
        if(No%i == 0 and i%2 == 1):
            factors.append(i)
    print(factors)

def main():
    tobj1 =threading.Thread(target=evenNumbers, args = (20,))
    tobj2 =threading.Thread(target=oddNumbers, args = (20,))
    tobj1.start()
    tobj2.start()
if __name__ == "__main__":
    main()