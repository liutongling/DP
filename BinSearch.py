
# 没有目标值查找的元素靠左
def binSearch(nums:list,l:int,r:int, target):
    left = l
    right = r
    while left<right:
        mid = (right+left)//2 + 1
        if nums[mid]>target:
            right = mid - 1
        else:
            left = mid
    return left




