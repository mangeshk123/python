import sys
import os

def isFilesAreEqual(args):
    fileName1 = args[1]
    fileName2 = args[2]
    if(os.path.getsize(fileName1) != os.path.getsize(fileName2)):
        return False
    else:    
        fobj1 = open(fileName1,"rb")
        fobj2 = open(fileName2,"rb")
        chunk_size = 1000
        while True:
            chunk1 = fobj1.read(chunk_size)
            chunk2 = fobj2.read(chunk_size)
            
            if chunk1 != chunk2:
                return False
            if not chunk1: # Reached end of files
                return True


def main():
    try:
        Ret = isFilesAreEqual(sys.argv)
        if(Ret):
            print("Files are equal")
        else:
            print("Files are Not equal")
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()