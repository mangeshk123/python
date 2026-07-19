def main():
    try:
        fobj = open("Demo.txt","r")        
        print("File gets opened")
        fdata = fobj.readlines()
        print(len(fdata))
        fobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()