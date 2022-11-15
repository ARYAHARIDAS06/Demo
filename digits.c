#include<stdio.h>
int main()
{
int num,r,sum=0;
printf("\n Enter a number");
scanf("%d",&num);
while(num>0)
{
  r=num%10;
  sum=sum+r;
  num=num/10;}
printf("sum of digits %d\n",sum);

return 0;
}
