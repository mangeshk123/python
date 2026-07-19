def main():
    flag = False
    VowelArray = ["A","E","I","O","U","a","e","i","o","u"]
    char = input("Input any character: ")
    for Vowel in VowelArray: # pyright: ignore[reportUndefinedVariable]
        if(char == Vowel):
            flag = True
    if(flag):  
        print("Entered Character is  Vowel")
    else:
        print("Entered Character is not Vowel")
        

if __name__ == "__main__":
    main()