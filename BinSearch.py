
# （1）没有目标值查找的元素靠左,如果有目标值返回目标值索引
# 思想：
"""
    思路如下如果当前
"""
def binSearch(nums:list, target):
    left = 0
    right = len(nums)-1
    while left<right:
        mid = (right+left)//2 + 1
        if nums[mid]>target:
            right = mid - 1
        else:
            left = mid
    return left
# （2）没有目标值查找的元素靠右,如果有目标值返回目标值索引

# （3）有目标值且重复查找的元素靠左
def binSearch_hadLeft(nums:list, target):
    left = 0
    right = len(nums)-1
    while left<right:
        mid = (right+left)//2
        if nums[mid]<target:
            left = mid + 1
        else:
            right = mid
    return left
# （4）有目标值且重复查找的元素靠右

# 库函数参考bisect https://docs.python.org/zh-cn/3/library/bisect.html

def findPeakElement(nums: list) -> int:
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2
        if nums[mid - 1] < nums[mid] and nums[mid] > nums[mid + 1]:
            return nums[mid]
        elif nums[mid] < nums[mid + 1]:
            l = mid + 1
        elif nums[mid] > nums[mid + 1]:
            r = mid
    return nums[mid]

def search1(nums: list, target: int) -> int:
    firstNum = nums[0]
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) // 2 + (l+r) % 2
        if target >=firstNum: #表示目标值是在第一部分
            if nums[mid] < firstNum:
                r = mid - 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] <= target:
                    l = mid
        else: # 目标值是在第二部分
            if nums[mid] > firstNum:
                l = mid + 1
            else:
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] <= target:
                    l = mid
    if l>=len(nums):
        return -1
    return l if nums[l] == target else -1

def search(nums: list, target: int) -> int:
    n = len(nums)
    if n==0:
        return -1
    if n==1:
        return 0 if nums[0]==target else -1
    l = 0
    r = n - 1
    firstNum = nums[0]
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target: return mid
        if firstNum<=nums[mid]:
            if firstNum <= target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] < target < firstNum:
                l = mid + 1
            else:
                r = mid - 1
    return -1
def pow1(number:int,exponent:int)->int:
    if exponent<0:
        exponent = -exponent
        number = 1/number
    if exponent==1:
        return number
    half = pow1(number,exponent//2)
    return half*half if exponent%2==0 else half*half*number

def pow2(number:int,exponent:int)->int:
    if exponent<0:
        exponent = -exponent
        number = 1/number
    l = number
    res = 1
    while exponent>0:
        if exponent%2==1:
            res = l * res
        exponent = exponent // 2
        l = l * l
    return res