weight=float(input("Enter WEIGHT in KGs-->"))
height=float(input("Enter HEIGHT in CMs-->"))
min_water=weight*.03
print("Min water you should drink is",min_water,"liters")
water=min_water+1.5
print("Max water you should drink is",water,"liters")
M=height/100
BMI=round(weight/(M*M),2)
ideal=round(weight/BMI*23,2)
diff=round(weight-ideal,2)
if diff>=0:
    print("You have to LOSE", diff, "KGs")
else: 
    print("You have to GAIN", abs(diff),"KGs")
print("Your Body Mass Index(BMI) is",BMI )
print("Your IDEAL weight should be",ideal)
print("Difference weight",diff)
if BMI<18.5:
    print("You are UNDER-WEIGHT")
elif BMI<25:
    print("You are NORMAL-WEIGHT")
elif BMI<30:
    print("You are OVER-WEIGHT")
else:
    print("You are OBESE")
    