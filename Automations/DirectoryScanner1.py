import sys
import os

def dirctortoryScanner(DirectoryPath):
    print("Files from directory are : ")
    for foldername,subfolder,filename in os.walk(DirectoryPath):
        for fname in filename:
            print(fname)

def main():
    Border = "-"*50
    print(Border)
    print("M automation script")
    print(Border)
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to travel the directory")
            print("for better usage please --u flag")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Please execute the script as ")
            print("python Filename.py <DirectoryName>")
            print("Directoryname should be absolute path")
        else:
            dirctortoryScanner(sys.argv[1])
    
    else:
        print("Invalid number of arguements")
        print("Please use --h or --u for more info")
    
    print(Border)
    print("Thank you")
    print(Border)
    
if __name__ == "__main__":
    main()