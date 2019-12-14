#This is a function to add numbers
def add(x,y) :
	return x+y

#this is a function to substract numbers
def substract(x,y):
	return x-y
	
def multiply(x,y):
	return x*y
	
def divide(x,y):
	return x/y	
	

print("enter number 1")
a=int(input())
print("enter number 2")
b=int(input())

#lets try some maths
print("adding",a," and",b," makes",add(a,b))
print("substracting",a," and",b," makes",substract(a,b))
print("multiplying",a," and",b," makes",multiply(a,b))
print("dividing",a," and",b," makes",divide(a,b))
