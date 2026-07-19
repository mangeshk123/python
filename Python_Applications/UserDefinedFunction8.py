# Accept: Multiple parameter
# Return: Multiple value
def BigBazaar():
    print("Inside BigBazar")
    def Amul():
        print("Inside Amul Ice cream parlour")
    

def main():
    BigBazaar() # Allowed
    Amul() # Error
    BigBazaar.Amul() # Error

if __name__ == "__main__" :
    main()