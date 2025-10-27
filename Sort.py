'''
    快速排序算法的实现
    快速排序算法除了“挖坑法”外，还有以下常见的方法来按照基准值区分元素：

1. 霍尔法（Hoare Partition Scheme）

思想：通过两个指针（左指针和右指针）从数组两端向中间移动，找到需要交换的元素。
步骤：

选择一个基准值（通常是数组的第一个元素）。
左指针从左向右移动，直到找到一个大于等于基准值的元素。
右指针从右向左移动，直到找到一个小于等于基准值的元素。
交换左右指针指向的元素，继续移动指针，直到左右指针相遇。


特点：交换次数较少，适合大规模数据。


2. Lomuto法（Lomuto Partition Scheme洛穆托）

思想：通过一个“分区指针”将数组分为两部分，小于基准值的放左边，大于基准值的放右边。
步骤：

选择一个基准值（通常是数组的最后一个元素）。
设置一个分区指针 i，初始值为数组的起始位置。
遍历数组，若当前元素小于基准值，则将其与分区指针指向的元素交换，并将分区指针右移。
遍历结束后，将基准值与分区指针指向的元素交换。


特点：实现简单，但交换次数较多。


3. 三指针法（Three-Way Partitioning）

思想：将数组分为三部分：小于基准值、等于基准值、大于基准值。
步骤：

选择一个基准值。
使用三个指针：low 指向小于基准值的区域末尾，mid 指向当前处理的元素，high 指向大于基准值的区域开头。
遍历数组：

若当前元素小于基准值，与 low 指针交换，low 和 mid 向右移动。
若当前元素等于基准值，仅 mid 向右移动。
若当前元素大于基准值，与 high 指针交换，high 向左移动。




特点：适合包含大量重复元素的数组，减少不必要的比较和交换。


总结

霍尔法：效率高，交换次数少，适合一般场景。
Lomuto法：实现简单，但交换次数较多。
三指针法：适合处理重复元素较多的数组。

每种方法都有其适用场景，选择时可以根据数据特点和实现需求来决定！



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

