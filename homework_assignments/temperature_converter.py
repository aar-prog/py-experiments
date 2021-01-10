print("This program is for converting Celsius to Farenheit \n")
print("Choose c for Celsius to Farenheit convertion")
print("Choose f for Farenheidt to Celsius convertion")
choice=input()
if choice=="c":
    c=float(input("What is the temparature in Celsius? \n"))
    f=9/5*c+32
    print(c,"Celsius is the same as",f,"Farenheit")
elif choice=="f":
    f=float(input("What is the temparature in Farenheit? \n"))
    c=(f-32)*5/9
    print(f,"Farenheit is the same as",c,"Celsius")

else:
    print("Invalid option")
















