#include <stdio.h>
#include "Head/greed.h"
int Fib[1000]; // 全局变量数组保存重叠子问题
int fibonacci(int n)
{
    if (n <= 1)
        return n;
    int tempL = Fib[n-1], tempR = Fib[n-2];
    if (tempL == 0)
    {
        tempL = fibonacci(n-1);
        Fib[n-1] = tempL;//每次计算完成都进行保存
    }
    if (tempR == 0)
    {
        tempR = fibonacci(n-2);
        Fib[n-2] = tempR;//每次计算完成都进行保存
    }
    return tempL + tempR;
}
int fibDp(int n)
{
    int fib[100] = {0};
    fib[0] = 0;
    fib[1] = 1;
    for (int i = 2; i <= n; i++)
    {
        fib[i] = fib[i-1] + fib[i-2];
    }
    return fib[n];
}
int main(void)
{
    // int arr[]={5,4,-1,7,8};
    // int result = Max_SonArr(arr,0,4);
    // printf("Max_SonArr(arr,0,15) = %d\n",result);
    for (int i = 1; i <= 20; i++)
    {
        int result = fibonacci(i);
        printf("%d\n", result);
    }

}