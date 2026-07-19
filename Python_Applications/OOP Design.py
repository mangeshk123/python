class Arithmatic:
    def __init__(self,A,B):
        self.No1 = A
        self.No2 = B

    def addition(self):
        return self.No1 + self.No2

    def substraction(self):
        return self.No1 - self.No2
    
print("Enter first number")
No1 = int(input())

print("Enter Second number")
No2 = int(input())

aObj = Arithmatic(No1,No2)

# addition(aObj, No1, No2)
print("Sum = ",aObj.addition())
print("Substraction = ",aObj.substraction())