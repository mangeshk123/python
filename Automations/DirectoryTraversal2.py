import os
def main():
    for FolderName, SubFolderName, Filename in os.walk("Marvellous"):
        print("FolderName :", FolderName)
        for subf in SubFolderName:
            print("SubFolderName :",subf)
    
if __name__ == "__main__":
    main()