class Arithmatic:

    def addition(No1,No2):
        return No1 + No2

    def substraction(No1,No2):
        return No1 - No2
    
aObj = Arithmatic()
print("Enter first number")
No1 = int(input())

print("Enter Second number")
No2 = int(input())

print("Sum = ",aObj.addition(No1,No2)) #Error
print("Substraction = ",aObj.substraction(No1,No2))