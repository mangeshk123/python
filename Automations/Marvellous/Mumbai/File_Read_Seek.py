# Seek(Where,From)

#From 0/1/2
# 0 = Start
# 1 = Current
# 2 = End
def main():
    try:
        fobj = open("Demo.txt","r")        
        print("File gets opened")

        fobj.seek(10,0)
        fData = fobj.read()
        print(fData)

        fobj.close()
    except FileNotFoundError as err:
        print("File is not present in current directory")

    
if __name__ == "__main__":
    main()