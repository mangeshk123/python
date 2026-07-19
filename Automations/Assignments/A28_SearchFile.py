import sys

def main():
    try:
        if(len(sys.argv) == 3):
            fobj = open(sys.argv[1],"r")
            searchString = sys.argv[2]
            print("File gets opened")
            fdata = fobj.read()
            words = list(fdata.split())
            flag = False
            for word in words:
                if(word == searchString):
                    flag = True
            if(flag):
                print("Entered String is present")
            else:
                print("Entered String is absent")
            fobj.close()
        
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()