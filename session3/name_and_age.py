names=["Aarush", "Anjali", "Krishna", "Sreelatha"]
ages=[9,6,35,32]
rows=len(names)
print(rows) #prints the number of the length of the list

print(names[0],"is",ages[0],"years old")
print(names[1],"is",ages[1],"years old")
print(names[2],"is",ages[2],"years old")
print(names[3],"is",ages[3],"years old")
print("-----------------------")

#Looping thrugh the lists
for a in names:
    print(a)
for b in ages:
    print(b)
print("-----------------------")
#Loop through both lists same time
for i in range(len(names)):
    #print(i)
    print(names[i],"is",ages[i],"years old")

print("-----------------------")
name=input("Enter your name:\n")
print(name)
print(len(name)) #prints the number of characters in my name
print("These are the first 3 letters of my name:",name[0:3]) 
print(name[::1])
print(name[::2])
print(name[::3])

#name="Aarush"
for a in name:
    print(a)


