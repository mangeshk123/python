def main():
    multi = 1
    num = int(input("Enter Number : "))
    for i in range(1,num + 1):
        multi = multi * i
    print("Factorial --------", multi)
    
if __name__ == "__main__":
    main()