a=int(input("enter a number"))
if a>0:
    print(a,"is positive")
elif a<0:
    print(a,"is negative")
else:
    print(a ,"is zero")
for i in range(0,10,2):
    print(i,end=" ")


for x in range(6):
    print(x)
    if x==3:
        break
else:
    print("finally finished")
