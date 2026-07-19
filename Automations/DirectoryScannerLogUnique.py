import sys
import os
import time

def dirctortoryScanner(DirectoryPath):
    timestamp = time.ctime()
    fobjName = "Marvellous%s.Log"%timestamp
    fobjName = fobjName.replace(" ", "_")
    fobjName = fobjName.replace(":", "_")
    print("Log file gets created with name :",fobjName) 
    fobj = open(fobjName,"w")
    fobj.write("Marvellous Automation script \n")
    fobj.write("Files from the directory are : \n")
    for foldername,subfolder,filename in os.walk(DirectoryPath):
        for fname in filename:
            fobj.write(fname + "\n")
    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("Marvellous automation script")
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
    print("Thank you for using Marvellous automation script")
    print(Border)
    
if __name__ == "__main__":
    main()