"""n=int(input("enter a number:"))
sum=(n*(n+1))/2
print(sum)
n=int(input("Enter a number: "))
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print("The sum of first n natural numbers is",sum1)"""
n=int(input("number count"))
x=[]
for n in range(0,n):
    x.append((int(input("enter numbers:"))))
print(x)
sum=0
for i in x:
    sum=sum+i
print(sum)
