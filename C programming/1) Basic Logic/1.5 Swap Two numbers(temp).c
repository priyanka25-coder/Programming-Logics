#include<stdio.h>
int main()
{
    int a,b,temp;
    printf("Enter 2 Numbers:\n");
    scanf("%d%d",&a,&b);
    printf("a = %d\tb = %d",a,b);
    printf("\nAfter swapping:\t");
     temp=a;
     a=b;
     b=temp;
     printf("a = %d\tb = %d",a,b);
}