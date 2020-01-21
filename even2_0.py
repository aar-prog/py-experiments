print("Enter the start")
y = int(input())
print("Start is " , y)
print("Enter the range")
z = int(input())
print("Range is " , z)
for x in range(y, z):
  if x%7 == 0:
    print(x)
