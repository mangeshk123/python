def pattern():
    pattern =""
    for i in range(1,22):
        if(i%2 == 0):
            pattern = pattern + f"{i}   "
    print(pattern)
    
def main():
    print(pattern())
    
if __name__ == "__main__" :
    main()