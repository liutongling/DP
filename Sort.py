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

def merge(arr1, arr2):
    i,j = 0,0
    result = []
    while i <len(arr1) and j <len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    while i < len(arr1):
        result.append(arr1[i])
        i += 1
    while j < len(arr2):
        result.append(arr2[j])
        j += 1
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr
    low, high = 0, len(arr)-1
    mid = (low+high)//2
    arr1 = mergeSort(arr[:mid+1])
    arr2 = mergeSort(arr[mid+1:])
    return merge(arr1, arr2)

