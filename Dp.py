# 小偷又发现了一个新的可行窃的地区。这个地区只有一个入口，我们称之为
#  root 。
#
#  除了
#  root 之外，每栋房子有且只有一个“父“房子与之相连。一番侦察之后，聪明的小偷意识到“这个地方的所有房屋的排列类似于一棵二叉树”。 如果 两个直接相连的
# 房子在同一天晚上被打劫 ，房屋将自动报警。
#
#  给定二叉树的 root 。返回 在不触动警报的情况下 ，小偷能够盗取的最高金额 。
#
#
#
#  示例 1:
#
#
#
#
# 输入: root = [3,2,3,null,3,null,1]
# 输出: 7
# 解释: 小偷一晚能够盗取的最高金额 3 + 3 + 1 = 7
#
#  示例 2:
#
#
#
#
# 输入: root = [3,4,5,1,3,null,1]
# 输出: 9
# 解释: 小偷一晚能够盗取的最高金额 4 + 5 = 9
#
#
#
#
#  提示：
#
#
#
#
#
#  树的节点数在 [1, 10⁴] 范围内
#  0 <= Node.val <= 10⁴
#
#
#  Related Topics 树 深度优先搜索 动态规划 二叉树 👍 2078 👎 0
import queue

from winerror import NOERROR


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 使用动态规划进行解决问题

class Solution(object):
    def __init__(self):
        f = {}
        g = {}
    def dfs(self,Node:TreeNode):
        if Node == None:
            self.f[None] = 0
            self.g[None] = 0
            return
        else:
            self.dfs(Node.right)
            self.dfs(Node.left)
            self.f[Node] = Node.val+self.g[Node.left] + self.g[Node.right]
            self.g[Node] = max(self.f[Node.left],self.g[Node.left]) + max(self.f[Node.right],self.g[Node.right])
    def rob(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # 使用队列遍历每层的结点数
        self.dfs(root)
        return max(self.f[root],self.g[root])









# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    sts = s.dfs()