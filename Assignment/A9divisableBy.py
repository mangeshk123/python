def main():
    qube = 0
    num = int(input("Enter Number : "))
    div = []
    for i in range(2,num):
        if(num%i == 0):
            div.append(i)
    print("Number is divisable by "  + str(div))

if __name__ == "__main__":
    main()