def main():
    try:
        fobj = open("Demo.txt","a")        
        print("File gets opened")
        fobj.write(" Pune Maharashtra ")
        fobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()