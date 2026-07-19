import os
def main():
    for FolderName, SubFolderName, Filename in os.walk("Marvellous"):
        for fname in Filename:
            print("Filename : ",fname)
    
if __name__ == "__main__":
    main()