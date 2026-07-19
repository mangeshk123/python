def CheckEven(no):
    if(no % 2 == 0):
        return True
    else:
        return False 
    

def main():
    value = int(input("Enter number :"))
    Even = CheckEven(value)
    if(Even):
        print("It's Even number")
    else:
        print("It's Odd number")

if __name__=="__main__":
    main()