def main():
    try:
        fobj = open("Demo.txt","r")        
        print("File gets opened")
        fdata = fobj.read()
        words = fdata.split()
        print(words)
        print(len(words))
        fobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()