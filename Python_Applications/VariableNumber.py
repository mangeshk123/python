def Display(*Data):
    print(Data)
    print(type(Data))

def main():
    Display(10,20,30,40,12.5,"Test", True,[10,20])

if __name__ == "__main__":
    main()