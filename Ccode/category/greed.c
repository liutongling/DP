//
// Created by liutongling on 2025/10/25. 最大子数组和
//
int left_MaxArr(int arr[],int s,int f)
{
    int ss = s;
    int ff = f;
    int maxNum=arr[f];
    int temp=arr[f];
    while (ff-1>=ss)
    {
        temp+=arr[ff-1];
        if (maxNum<temp)
            maxNum=temp;
        ff-=1;
    }

    return maxNum;

}
int right_MaxArr(int arr[],int s,int f)
{
    int ss = s;
    int ff = f;
    int temp=arr[s];
    int maxNum=arr[s];
    while (ss+1<=ff)
    {
        temp+=arr[ss+1];
        if (temp>maxNum)
            maxNum=temp;
        ss+=1;
    }
    return maxNum;
}
int Max_SonArr(int a[],int s,int f)
{
    if (s==f)
        return a[s];
    else
    {
        int mid = (s+f)/2;
        int max1 = Max_SonArr(a,s,mid);
        int max2 = Max_SonArr(a,mid+1,f);
        int left = left_MaxArr(a,s,mid);
        int right = right_MaxArr(a,mid+1,f);
        int max3 = left_MaxArr(a,s,mid)+right_MaxArr(a,mid+1,f);
        int temp = (max1>max2?max1:max2);
        return temp>max3?temp:max3;
    }
}