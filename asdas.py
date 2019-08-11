x=input()
a=""
b=""
for i in range(len(x)):
    if x[i].isdigit():
        a=x[i]
        print(a,end="")
    else:
        b=x[i]
