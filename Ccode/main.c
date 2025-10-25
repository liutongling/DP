#include <stdio.h>
#include "Head/greed.h"

int main(void)
{
    int arr[]={13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7};
    int result = Max_SonArr(arr,0,15);
    printf("Max_SonArr(arr,0,15) = %d\n",result);
}