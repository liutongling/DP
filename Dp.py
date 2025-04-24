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

#from PyQt5.QtXml.QXmlSimpleReader import setFeature
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

    # 给你两个正整数
    # low
    # 和
    # high 。
    #
    # 对于一个由
    # 2 * n
    # 位数字组成的整数
    # x ，如果其前
    # n
    # 位数字之和与后
    # n
    # 位数字之和相等，则认为这个数字是一个对称整数。
    #
    # 返回在[low, high]
    # 范围内的
    # 对称整数的数目 。
    #
    #
    #
    # 示例
    # 1：
    #
    # 输入：low = 1, high = 100
    # 输出：9
    # 解释：在
    # 1
    # 到
    # 100
    # 范围内共有
    # 9
    # 个对称整数：11、22、33、44、55、66、77、88
    # 和
    # 99 。
    # 示例
    # 2：
    #
    # 输入：low = 1200, high = 1230
    # 输出：4
    # 解释：在
    # 1200
    # 到
    # 1230
    # 范围内共有
    # 4
    # 个对称整数：1203、1212、1221
    # 和
    # 1230 。
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res = 0
        for i in range(low,high+1):
            temp = i
            t = []
            while temp!=0:
                k = temp % 10
                temp = temp // 10
                t.append(k)
            count = 0
            if len(t) %2 ==0:
                for j in range(len(t)//2):
                    count += (t[j] - t[len(t)-j-1])
                if count  == 0:
                    res += 1
        # print(res)
        return res

    def checkDynasty(self, places: list) -> bool:
        temp = places.sort()
        count = 0
        for i in range(4):
            if places[i]==0:
                count += 1
            else:
                if places[i+1] == places[i]:
                    return False
                count -= (places[i+1] - places[i]-1)

        return True if count>=0 else False

    def countGoodNumbers(self, n: int) -> int:

        return self.myPow(5,(n+1)//2)*self.myPow(4,n//2)

    def dfsPow(self,x:float,n:int):
        if n == 1:
            return x
        if n == 0:
            return 1

        return self.dfsPow(x,(n+1)//2)*self.dfsPow(x,n//2)


    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x=1/x
            n = -n
        return self.dfsPow(x,n)

    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x=1/x
            n = -n
        return self.dfsPow(x,n)

    def countGoodTriplets(self, arr: list, a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n-2):
            for j in range(i+1,n-1):
                for k in range(j+1,n):
                    if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                        print([arr[i],arr[j],arr[k]])
                        count += 1
        return count

    def countPairs(self, nums: list, k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j%k)==0:
                    count+=1
        return count
    def maxSubArray(self, nums: list) -> int:
        n = len(nums)
        res = min(nums) * len(n)
        for i in range(n):
            count = 0
            for j in range(i,n):
                count += nums[j]
                if res < count:
                    res = count
        return res
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        dp = [0] * n
        for j in range(n):
            if s[j] == ')':
                if j >0  and s[j-1] == '(':
                    dp[j] = dp[j-2] + 2
                elif j-dp[j-1]-1 >= 0 and s[j-dp[j-1]-1] == '(':
                    dp[j] = dp[j-1] + 2 + dp[j-dp[j-1]-2]
        return max(dp)
# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    val = s.longestValidParentheses('(()()()()(((()))')
    print(val)