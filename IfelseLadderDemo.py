# Age less than 5 free
# Age greater than 5 and less than eq to 18 -- 900 rs
# Age greater than 18 and less than eq to 40 -- 1200 rs
# Age greater than 40 -- 500 rs

print("---------------------------------------------------------------------")
print("-----------------Amusement park Ticket Counter-----------------------")
print("---------------------------------------------------------------------")

print("Enter your Age: ")
Age = int(input())

if (Age>0 and Age <=5):
    print("Free entry")
elif (Age > 5 and Age <= 18):
    print("You need to pay 900 rs")
elif (Age > 18 and Age <= 40):
    print("You need to pay 1200 rs")
else:
    print("You need to pay 500 rs")
