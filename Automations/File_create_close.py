def main():
    try:
        fobj = open("Demo.txt","w")
        print("File gets opened")
        fobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()