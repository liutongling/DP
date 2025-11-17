from Dp import tower_math
import bisect
import math
from Dijkstra import Dijkstra1
from BinSearch import *
from Prim import Prim, Graph, prim_mst
from greed import *
from recursion import *
from Sort import *
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def minDepth(self, root: TreeNode) -> int:
#         if root.left == None and root.right==None:
#             return 1
#         else:
#             if root.left != None and root.right!=None:
#                 return min(self.minDepth(root.left)+1,self.minDepth(root.right)+1)
#             elif root.right !=None and root.left==None:
#                 return self.minDepth(root.right)+1
#             elif root.right==None and root.left!=None:
#                 return  self.minDepth(root.left)+1
#     def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
#         if root ==None:
#             return False
#         def dfs(root:TreeNode,Sum:int)->bool:
#             if root.left==None and root.right==None:
#                 return True if Sum==root.val else False
#             else:
#                 lr = False
#                 ll = False
#                 Sum -= root.val
#                 if root.left !=None:
#                     ll = dfs(root.left,Sum)
#                 if root.right!=None:
#                     lr = dfs(root.right,Sum)
#                 return lr or ll
#         return dfs(root,targetSum)
#     def Complete_BackPack(self,W:list,C:list,M:int) -> int:
#         # 创建一个二维表格并且初始化好边界
#         row = len(W)+1
#         col = M+1
#         dp = [[0 for i in range(col)] for j in range(row)]
#
#         # 开始更新状态表格
#         for i in range(1,row):
#             for j in range(1,col):
#                 k = j//W[i-1]
#                 temp = 0
#                 while k>=0:
#                     temp= dp[i-1][j-k*W[i-1]]+k*C[i-1] if temp < dp[i-1][j-k*W[i-1]]+k*C[i-1] else temp
#                     k-=1
#                 dp[i][j] = temp
#         print(dp)
#         return dp[row-1][col-1]
#
#
# def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
#     i = bisect(breakpoints, score)
#     print(i)
#     return grades[i]
class Solution:
    def lengthOfLIS_Force(self, nums: list) -> int:
        # 暴力解决
        maxCount = 0
        for i in range(len(nums)):
            count = 1
            temp = nums[i]
            k = i
            while k < len(nums):
                if temp < nums[k]:
                    count += 1
                    temp = nums[k]
                k += 1
            if count > maxCount:
                maxCount = count
        return maxCount
    def lengthOfLIS(self, nums: list) -> int:
        # 暴力解决
        maxCount =[0]*len(nums)
        maxCount[-1] = 1
        for i in range(len(nums)-1,-1,-1):
            maxcount = 0
            for j in range(len(nums)-1,i,-1):
                if nums[j]>nums[i] and maxcount < maxCount[j]:
                    maxcount = maxCount[j]
            maxCount[i] = maxcount + 1


        return max(maxCount)



if __name__ == '__main__':
    # G = [[0, 20, math.inf, math.inf, math.inf, 15, math.inf],
    #      [20, 0, 13, math.inf, math.inf, math.inf, math.inf],
    #      [math.inf, 13, 0, 18, math.inf, math.inf, 23],
    #      [math.inf, math.inf, 18, 0, 7, math.inf, math.inf],
    #      [math.inf, math.inf, math.inf, 7, 0, 26, math.inf],
    #      [15, math.inf, math.inf, math.inf, 26, 0, 9],
    #      [math.inf, math.inf, 23, math.inf, math.inf, 9, 0],
    #      ]
    # G = [[0, 1, math.inf, math.inf, math.inf, 1, math.inf],
    #      [1, 0, 1, math.inf, math.inf, math.inf, math.inf],
    #      [math.inf, 1, 0, 20, math.inf, math.inf, 1],
    #      [math.inf, math.inf, 20, 0, 20, math.inf, math.inf],
    #      [math.inf, math.inf, math.inf, 20, 0, 20, math.inf],
    #      [1, math.inf, math.inf, math.inf, 20, 0, 1],
    #      [math.inf, math.inf, 1, math.inf, math.inf, 1, 0],
    #      ]
    # M = 7
    # primTest = Prim(M,G)
    # result = primTest.prim_work()
    # print(result)

    g = Dijkstra1(5)
    g.add_edge(0, 1, 20)
    g.add_edge(0, 3, 60)
    g.add_edge(0, 4, 15)
    g.add_edge(1, 2, 42)
    g.add_edge(3, 2, 30)
    g.add_edge(4, 3, 23)

    g.dijkstra_work(0)

    # s=Solution()
    # r =  s.lengthOfLIS([0,1,0,3,2,3])# tower_math([[2],[6,9],[8,2,0],[4,6,7,3],[6,5,2,1,5]])
    # print(r)