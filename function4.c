#include<stdio.h>
void myFunction(int a){
printf("a in fun1 is%d",a);
a=55;
printf("a in fun2 is %d",a);
}
void main(){
int a=3;
printf("a in main2 =%d",a);
myFunction(a);
printf("a in main2 =%d",a);
}
