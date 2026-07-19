def pattern(No):
    pattern =""
    for i in range(No):
        pattern = pattern + "*   "
    print(pattern)
    
def main():
    print("Enter any number")
    Num = int(input())
    print(pattern(Num))
    
if __name__ == "__main__" :
    main()