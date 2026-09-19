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
        duplicate = {}
        for fname in filename:
            fname = os.path.join(foldername,fname)
            CheckSum = calculateCheckSum(fname)
            if(CheckSum in duplicate):                
                duplicate[CheckSum].append(fname)
            else:
                duplicate[CheckSum] = [fname]
    return duplicate
    
def deleteDuplicate(Directory):
    MyDict = findDuplicate(Directory)
    Result = list(filter((lambda x : len(x)>1), MyDict.values()))
    Count = 0
    TotalDeleted = 0
    for value in Result:
        for subValue in value:            
            Count = Count + 1
            if(Count > 1):
                TotalDeleted = TotalDeleted + 1
                os.remove(subValue)            
        Count = 0
    print("Total Deleted file :", TotalDeleted)        
    
    
def main():
    deleteDuplicate("Test")
    
if __name__ == "__main__":
    main()