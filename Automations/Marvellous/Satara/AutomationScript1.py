import sys
def main():
    if(len(sys.argv) == 2):
        DirectoryName = sys.argv[1]
        print(len(sys.argv))
        print("Directory name is ", DirectoryName)
if __name__ == "__main__":
    main()