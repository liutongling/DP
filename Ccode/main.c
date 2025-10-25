#include <stdio.h>
#include "Head/greed.h"

int main(void)
{
    int arr[]={5,4,-1,7,8};
    int result = Max_SonArr(arr,0,4);
    printf("Max_SonArr(arr,0,15) = %d\n",result);
}