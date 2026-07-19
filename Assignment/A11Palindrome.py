def isPalindrome(No):
    NoClone = No
    Rem = 0
    ReversedNo = 0
    while NoClone > 0:
        Rem = NoClone % 10
        ReversedNo = ReversedNo * 10 + Rem 
        NoClone = int(NoClone / 10)
    
    return ReversedNo == No
        
def main():
    print("Enter any number")
    No = int(input())
    Ret = isPalindrome(No)
    if Ret:
        print("Entered number is palindrome")
    else:        
        print("Entered number is not palindrome")
    
if __name__ == "__main__" :
    main()