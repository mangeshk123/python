import sys
import os
def main():
    try:
        fileName = sys.argv[1]
        tragetName = sys.argv[2]
        if(os.path.exists(fileName)):
            fobj = open(fileName,"r")
            tobj = open(tragetName,"w")
            tobj.write(fobj.read())
            
        else:
            print("File does not exists")
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()