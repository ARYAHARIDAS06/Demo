#include<stdio.h>
int myFunction(int x, int y){
return (x+y);
}
int main(){
int x,y;
printf("enter two numbers:");
scanf("%d%d",&x,&y);
int result = myFunction(x,y);
printf("Result is = %d",result);
return 0;
}
