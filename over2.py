list=[]
n=int(input("enter a number of elements"))
for i in range(0,n):
    list.append(int(input()))
for i in range(0,n):
   if list[i]>100:
        list[i]="over"       
print(list)
