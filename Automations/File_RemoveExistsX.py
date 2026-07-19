import os
def main():
    if(os.path.exists("Demo.txt")):
        print("File is present in current dirctory")
    else:
        print("File is not present in current dirctory")

    
if __name__ == "__main__":
    main()