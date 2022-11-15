#include<stdio.h>
void main()
{
int myAge = 43;
printf("%d",myAge);
printf("%p",&myAge);
int *ptr=&myAge;
printf("%d\n",myAge);
printf("%p\n",&myAge);
printf("%p\n",ptr);
}

