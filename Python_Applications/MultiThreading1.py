import threading
def display():
    print("Inside Display: ", threading.get_ident())
    
def main():
    print("Inside main: ", threading.get_ident())
    display()

if __name__ == "__main__":
    main()