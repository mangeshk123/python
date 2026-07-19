
#########################################################
#
#   Importing required libraries
#
#########################################################
import sys
import os
import time
import schedule

#########################################################
#
#   Function Name:      dirctortoryScanner
#   Input:              Directory Path
#   Description:        Deletes empty files
#   Date:               19/07/2026
#   Author:             Mangesh Kulkarni
#
#########################################################

def dirctortoryScanner(DirectoryPath):
    Border = "-"*40
    timestamp = time.ctime()
    fobjName = "Marvellous%s.Log"%timestamp
    fobjName = fobjName.replace(" ", "_")
    fobjName = fobjName.replace(":", "_")

    Ret = False
    Ret = os.path.exists(DirectoryPath)
    
    if(Ret == False):
        print("Marvellous Automation error : There is no such directory with name ", DirectoryPath )
        return
    
    Ret = os.path.isdir(DirectoryPath)
    if(Ret == False):
        print("Marvellous Automation error : It is not a directory with name : ", DirectoryPath )
        return
    
    print("Log file gets created with name :",fobjName) 
    fobj = open(fobjName,"w")
    fobj.write(Border + "\n\n")
    fobj.write("Marvellous Automation script \n")
    fobj.write(Border + "\n\n")
    fobj.write("Files from the directory are : \n\n")
    fobj.write(Border + "\n")
    TotalFiles = 0
    EmptyFiles = 0
    for foldername,subfolder,filename in os.walk(DirectoryPath):
        for fname in filename:
            TotalFiles = TotalFiles + 1
            fname = os.path.join(foldername,fname)
            fobj.write(f"{fname} : {os.path.getsize(fname)}\n")
            if(os.path.getsize(fname) == 0):
                EmptyFiles = EmptyFiles + 1
                os.remove(fname)
    fobj.write(Border + "\n")
    fobj.write(f"Total files scanned :{TotalFiles}\n")
    fobj.write(f"Total Empty files found and deleted:{ EmptyFiles }\n")
            
    fobj.write(Border + "\n")
    fobj.write("Log file gets created at :"+ timestamp)
    fobj.write("\n" + Border + "\n")
    fobj.close()

#########################################################
#
#   Function Name:      main()
#   Input:              Directory Path
#   Description:        Deletes empty files
#   Date:               19/07/2026
#   Author:             Mangesh Kulkarni
#
#########################################################

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
            schedule.every(1).minute.do(dirctortoryScanner,sys.argv[1])
            while(True):
                schedule.run_pending()
                time.sleep(1)
    
    else:
        print("Invalid number of arguements")
        print("Please use --h or --u for more info")
    
    print(Border)
    print("Thank you for using Marvellous automation script")
    print(Border)

#########################################################
#
#   Starter of script
#
#########################################################

if __name__ == "__main__":
    main()