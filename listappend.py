n=int(input("number count"))
x=[]
for i in range(0,n):
    x.append((int(input("enter numbers:"))))
print(x)
for i in range(0,n):
    if x[i]>100:
        x[i]="over"
print(x)
