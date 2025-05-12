import math

from intake.util_tests import temp_conf


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
        def dfs(root:TreeNode,Sum:int)->bool:
            if root==None:
                return True if Sum==0 else False
            else:
                Sum -= root.val
                return (dfs(root.left,Sum) or dfs(root.right,Sum))
        #temp = dfs(root)
        return dfs(root)

if __name__ == '__main__':
    snode1 = TreeNode(2)
    snode2 = TreeNode(3)
    snode3 = TreeNode(4)
    snode4 = TreeNode(5)
    snode5 = TreeNode(6)
    snode1.right = snode2
    snode2.right = snode3
    snode3.right = snode4
    snode4.right = snode5
    s = Solution()
    print(s.minDepth(snode1))