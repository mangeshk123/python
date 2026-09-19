import sys
import os
import hashlib

def calculateCheckSum(FileName):
    fobj = open(FileName,"rb")
    hobj = hashlib.md5()
    Buffer = fobj.read(1024)
    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)
    fobj.close()
    return hobj.hexdigest()

def findDuplicate(directoryName):
    Ret = False
    Ret = os.path.exists(directoryName)
    
    if(Ret == False):
        print("path is invalid")
        return
    
    Ret = os.path.isdir(directoryName)

    if(Ret == False):
        print("It is not a directory")
        return
    Unique = 0
    Same = 0
    Total = 0
    for foldername,subfolder,filename in os.walk(directoryName):
        duplicate = {}
        for fname in filename:
            fname = os.path.join(foldername,fname)
            CheckSum = calculateCheckSum(fname)
            Total = Total + 1
            print(f"{fname} : {CheckSum}")
            if(CheckSum in duplicate):                
                Same = Same + 1
                duplicate[CheckSum].append(fname)
            else:
                Unique= Unique + 1
                duplicate[CheckSum] = [fname]
    print("Total files scanned :", Total)
    print("Uniquew files found :", Unique)
    print("Duplicate files found :", Same)   
    
def main():
    findDuplicate("Test")

if __name__ == "__main__":
    main()