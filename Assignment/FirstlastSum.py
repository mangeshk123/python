def main():
    arr = [1,2,3,4]
    min = 0
    max = 0
    for no in arr:
        if(min == 0 or min > no):
            min = no
        if(max == 0 or max < no):
            max = no
    print("Sum", min + max)



if __name__ == "__main__":
    main()