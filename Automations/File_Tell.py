def main():
    try:
        fobj = open("Demo.txt","r")        
        print("File gets opened")
        print("File offset is", fobj.tell())
        fdata = fobj.read(10)
        print(fdata)
        print("File offset is", fobj.tell())
        fobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()