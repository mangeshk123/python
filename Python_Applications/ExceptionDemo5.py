

def main():
    Ans = 0
    try :
        print("Enter first number")
        No1 = int(input())

        print("Enter second number")
        No2 = int(input())

        Ans = No1 / No2
        print("Division is successfull")
    except Exception as eobj:
        print("Exception occured :",eobj)
    except ZeroDivisionError as zobj:
        print("Exception occured due to second oprand is zero :",zobj)
    except ValueError as vobj:
        print("Exception occured due to invlid datatype :",vobj)

    print("Result is ", Ans)

if __name__ == "__main__" :
    main()