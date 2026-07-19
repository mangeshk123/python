import sys
def main():
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("HELP")
        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("USAGE")
        else:
            DirectoryName = sys.argv[1]
            print("Directory name is : ",DirectoryName)
    else:
        print("Invalid number of arguements")
        print("Please use --h or --u for more info")

if __name__ == "__main__":
    main()