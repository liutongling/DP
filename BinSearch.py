
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
    if exponent == 0:
        return 1
    if exponent==1:
        return number
    half = pow1(number,exponent//2)
    return half*half if exponent%2==0 else half*half*number

def pow2(number:int,exponent:int)->int:
    if exponent<0:
        exponent = -exponent
        number = 1/number
    lowNum = number
    res = 1
    while exponent>0:
        if exponent%2==1:
            res = lowNum * res
        exponent = exponent // 2
        lowNum = lowNum * lowNum
    return res

# 使用二分法找到数组中的最大值和最小值
def select_minAndMax(nums:list)->tuple:
    if len(nums)==1:
        return nums[0], nums[0]
    else:
        mid = len(nums)//2
        min1, max1 = select_minAndMax(nums[:mid])
        min2, max2 = select_minAndMax(nums[mid:])
        return min1 if min1<min2 else min2, max1 if max1>max2 else max2

# 最大子数组

def max_array(nums:list)->int: # 使用动态规划的解法

    max_numbers=nums[0]
    next_numbers=nums[0]
    for num in range(1,len(nums)):
        if nums[num]+next_numbers>nums[num]:
            next_numbers = nums[num]+next_numbers
        else:
            next_numbers = nums[num]
        if next_numbers>max_numbers:
            max_numbers = next_numbers
    return max_numbers


def max_array1(nums: list) -> int:  # 使用暴力求解算法
    maxSum = 0
    tempArr = [0, 0]
    for i in range(len(nums)):
        tempSum = 0
        for j in range(i,len(nums)):
            tempSum += nums[j]
            if tempSum>maxSum:
                maxSum = tempSum
                tempArr[0] = i
                tempArr[1] = j
    return tempArr

