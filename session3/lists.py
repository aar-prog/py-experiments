subs=["math", "science", "language", "social studies"]
marks=[125,105,75,55]
num=len(subs)
MAX=150
for i in range(num):
    p=marks[i]/MAX*100
    if p<35:
        grade="F"
    elif p<50:
        grade="C"
    elif p<60:
        grade="B"
    elif p<80:
        grade="A"
    else:
        grade="S+"
    print("-%-15s %3d %3d"%(subs[i],marks[i],MAX),end=" ")
    print("%3d%% %-3s"%(p,grade))
print("loop is over")
