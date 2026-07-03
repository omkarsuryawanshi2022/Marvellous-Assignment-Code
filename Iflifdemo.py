print("__________________________")
print("__________   ticket prising software ______________")
print("enter the Age:")
Age = int(input())

if(Age<5):
    print("Your ticket is free")

elif (Age<5 and Age>=18):
    print("Ticket prise : 900")

elif(Age<=18 and Age>=40):
    print("Ticket prise is : 1200")

else:
    print("Ticket prise is :500")
