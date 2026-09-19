import sys
import os

countOfString = lambda sum,no : sum + no

def main():
    FileName = sys.argv[1]
    SearchString = sys.argv[2]
    fobj = open(FileName, "r")
    fdata = fobj.read()
    wordlist = fdata.split()
    result = list(filter(lambda x: x == SearchString, wordlist))
    print(len(result))
    
if __name__ == "__main__":
    main()