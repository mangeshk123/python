def isVowel(Char):
    VowelChars =["A","E","I","O","U","a","e","i","o","u"]
    for vchar in VowelChars:
        if(vchar == Char):
            return True
    return False

def main():
    print("Enter any number")
    Character = input()
    Ret = isVowel(Character)
    if Ret:
        print("Entered Char  is Vowel")
    else:        
        print("Entered Char is not Vowel")
    
if __name__ == "__main__" :
    main()