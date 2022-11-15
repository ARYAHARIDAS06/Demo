#include<stdio.h>
void main()
{
int a,b,c;
printf("\n Enter three numbers");
scanf("%d%d%d",a,b,c);
if(a>b&&a>c)
printf("\n%d a is greater",a);
else if(b>c)
printf("\n%d b is greater",b);
else
printf("\n%d c is greater",c);
}
