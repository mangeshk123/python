def divisableBy5(No):
    if No %5 == 0:
        return True
    else:
        return False
    
def main():
    print("Enter any number")
    Num = int(input())
    print(divisableBy5(Num))
    
if __name__ == "__main__" :
    main()