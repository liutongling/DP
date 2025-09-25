'''
    快速排序算法的实现
'''
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    low, high = 0, len(arr)-1
    pivot = arr[low]
    while low < high:
        while low < high and arr[high] > pivot:
            high -= 1
        while low < high and arr[low] <= pivot:
            low += 1
        arr[low], arr[high] = arr[high], arr[low]
    arr1 = quickSort(arr[0:high+1])
    arr2 = quickSort(arr[high+1:])
    arr1.extend(arr2)
    return arr1