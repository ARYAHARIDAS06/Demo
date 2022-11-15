#include<stdio.h>
void main()
{
int a[3]={1,2,3};
int b[10],i;
printf("enter the values for array b\n");
for(i=0;i<10;i++)
{
b[i]=i;
}
printf("value in a[2] %d\n",a[2]);
printf("value in array b\n");
for(i=0;i<10;i++)
printf("%d",b[i]);
}
