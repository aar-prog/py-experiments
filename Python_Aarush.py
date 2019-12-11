#!/usr/bin/env python3

print("Hello, world!")
x=1
y=0

if x==y:
  print("y=",y)
  print("x=",x)

if x>y:
  print("x=",x)

if x<y:
  print("y=",y)


mystring = 'bye'
print(mystring)

mystring = "Why don't you need to worry about apostrophes??!?"
print(mystring)

one = 1
two = 2
three = one + two
print(three)

hello = "2+2=4-"
world = "1=3"
bye = "Yay i know math"




never = "I know Python yaaaaay!"
tryagain = "Wrote by Aarush"
helloworldbyenevertryagain = hello + " " + world + " " + bye + " " + never + " " + tryagain
print(helloworldbyenevertryagain)

aa, an = 11, 8
print(aa,an)

aa = 11 
an = 8
says = "aa is older than an"

print(aa , an , says)

aa = 11
an = 8
says = "Together aa + an count up to"

print(says , aa + an)

mystring = "run"
myfloat = 10.0
myint = 20 

# testing code
if mystring == "run":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)

mylist = []
mylist.append(11)
mylist.append(22)
mylist.append(33)
print(mylist[0]) # prints 11
print(mylist[1]) # prints 22
print(mylist[2]) # prints 33

# prints out 11,22,33
for x in mylist:
    print(x)

mylist = [1,2,3,4,5,6,7,8,9,10]
#print(mylist[0])
total=0
for x in mylist:
    total=total+x
    print(x,total)

print("Bye, see you next time.")

print("Hi, we are back!")

number = 1 + 2 * 3 / 4.0
print(number)

remainder = 15 % 0.35
print(remainder)

squared = 21 ** 2
cubed = 99921999999999999921999921 ** 21
print(squared)
print(cubed)

