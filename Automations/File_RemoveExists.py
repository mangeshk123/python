import os
def main():
    ret = os.path.exists("Demo.txt")
    if(ret == True):
        print("File is present in current dirctory")
        os.remove("Demo.txt")
    else:
        print("File is not present in current dirctory")

    
if __name__ == "__main__":
    main()