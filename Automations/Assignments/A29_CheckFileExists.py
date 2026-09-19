import sys
import os
def main():
    try:
        fileName = sys.argv[1]
        if(os.path.exists(fileName)):
            print("File exists")
        else:
            print("File does not exists")
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()