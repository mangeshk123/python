import threading
def display(No):
    print(f"Inside Display {No}: ", threading.get_ident())
    
def main():
    print("Inside main: ", threading.get_ident())
    tobj =threading.Thread(target=display, args = (10,))
    tobj.start()

if __name__ == "__main__":
    main()