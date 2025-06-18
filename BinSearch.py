
# （1）没有目标值查找的元素靠左,如果有目标值返回目标值索引
# 思想：
"""
    思路如下如果当前
"""
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
# （2）没有目标值查找的元素靠右,如果有目标值返回目标值索引

# （3）有目标值且重复查找的元素靠左

# （4）有目标值且重复查找的元素靠右

# 库函数参考bisect https://docs.python.org/zh-cn/3/library/bisect.html