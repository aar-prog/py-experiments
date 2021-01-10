a,op,b=(input("Enter 2 nums & op like 2 * 3--> ")).split()
a=float(a)
b=float(b)
print(a,op,b)
if op=="+":
    print("sum=",round(a+b,2))
elif op=="-":
    print("difference=",round(a-b,2))
elif op=="*":
    print("product=",round(a*b,2))
elif op=="/":
    print("quotient=",round(a/b,2))
else:
    print(op,"Is an invalid operator. Try again")


print(year/400,"Year divided by 400") 
print(year%4,"Year modolus of 4")
print(year%400,"Year modolus of 400")
print(year%100,"Year modolus of 100")
print(year/4,"Year divided by 4")