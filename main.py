import math
from bisect import bisect
from collections import Counter
from numpy.lib.polynomial import roots
from EverDay import EverDay, FirstUnique
from bound import branch_and_bound_knapsack
from bound import bound
import numpy as np

from draw import Draw
from BinSearch import binSearch
from kmp import build_next,compute_next_array

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root.left == None and root.right==None:
            return 1
        else:
            if root.left != None and root.right!=None:
                return min(self.minDepth(root.left)+1,self.minDepth(root.right)+1)
            elif root.right !=None and root.left==None:
                return self.minDepth(root.right)+1
            elif root.right==None and root.left!=None:
                return  self.minDepth(root.left)+1
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if root ==None:
            return False
        def dfs(root:TreeNode,Sum:int)->bool:
            if root.left==None and root.right==None:
                return True if Sum==root.val else False
            else:
                lr = False
                ll = False
                Sum -= root.val
                if root.left !=None:
                    ll = dfs(root.left,Sum)
                if root.right!=None:
                    lr = dfs(root.right,Sum)
                return lr or ll
        return dfs(root,targetSum)
    def Complete_BackPack(self,W:list,C:list,M:int) -> int:
        # 创建一个二维表格并且初始化好边界
        row = len(W)+1
        col = M+1
        dp = [[0 for i in range(col)] for j in range(row)]

        # 开始更新状态表格
        for i in range(1,row):
            for j in range(1,col):
                k = j//W[i-1]
                temp = 0
                while k>=0:
                    temp= dp[i-1][j-k*W[i-1]]+k*C[i-1] if temp < dp[i-1][j-k*W[i-1]]+k*C[i-1] else temp
                    k-=1
                dp[i][j] = temp
        print(dp)
        return dp[row-1][col-1]


def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    print(i)
    return grades[i]
if __name__ == '__main__':
    # Draw(720,0,0,1,0,0,2,10)
    # ss = build_next("ABACABAB")
    ss = build_next("ABAACABAAT")
    sss = compute_next_array("ABACABAB")
    print(ss)
    # print(sss)