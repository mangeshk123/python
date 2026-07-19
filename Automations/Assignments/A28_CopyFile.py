def main():
    try:

        fileName  = input("Enter Filename :")
        targetfileName  = input("Enter target Filename :")

        fobj = open(fileName,"r")
        tfobj = open(targetfileName,"w")        
        print("File gets opened")
        fdata = fobj.read()
        print(fdata)
        tfobj.write(fdata)
       
        fobj.close()
        tfobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()