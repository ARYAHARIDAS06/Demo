n=int(input("number count"))
x=[]
for n in range(0,n):
    x.append((int(input("enter numbers:"))))
print(x)
result=[]
for i in x:
    if i>100:
        result.append("over")
    else:
        result.append(i)
    print(result)
