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
    
    for foldername,subfolder,filename in os.walk(directoryName):
        for fname in filename:
            fname = os.path.join(foldername,fname)
            CheckSum = calculateCheckSum(fname)
            print(f"{fname} : {CheckSum}")
    
def main():
    findDuplicate("Test")

if __name__ == "__main__":
    main()