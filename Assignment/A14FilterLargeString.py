minLength = lambda s: len(s) > 5

def main():
    Strings = ["test","test1","test12","test123","test1234"]
    fData = list(filter(minLength,Strings))
    print(fData)

if __name__ == "__main__" :
    main()