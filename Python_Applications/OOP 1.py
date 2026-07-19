class Arithmatic:

    def addition(self,No1,No2):
        return No1 + No2

    def substraction(self,No1,No2):
        return No1 - No2
    
aObj = Arithmatic()
print("Enter first number")
No1 = int(input())

print("Enter Second number")
No2 = int(input())

# addition(aObj, No1, No2)
print("Sum = ",aObj.addition(No1,No2))
print("Substraction = ",aObj.substraction(No1,No2))