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
from functools import cache
from math import inf

from Dijkstra import Dijkstra
from Prim import Prim
from kruskal import Kruskal
from pywin32_testutil import testmain
#from PyQt5.QtXml.QXmlSimpleReader import setFeature
from winerror import NOERROR
from queue import PriorityQueue

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
    # 2176. 统计数组中相等且可以被整除的数对
    def countPairs(self, nums: list, k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j%k)==0:
                    count+=1
        return count
    def countPairs1(self, nums: list, k: int) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j] and (i*j%k)==0:
                    count+=1
        return count
    # 2176. 统计数组中相等且可以被整除的数对
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
    # 有效括号的动态规划写法
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

    def maxSubArray(self, nums: list) -> int:
        current_max = nums[0]
        global_max = nums[0]
        for i in range(1,len(nums)):
            current_max = max(current_max,current_max+nums[i])
            global_max = max(global_max,current_max)
        return global_max

    def countSubarrays(self, nums: list) -> int:
        n = len(nums)
        count = 0
        for i in range(n-3):
            if (nums[i] + nums[i+2])*2 == nums[i+1]:
                count += 1
        return count
    # 乘船问题
    #
    def min_boats(self,people, limit):
        people.sort()
        left = 0
        right = len(people) - 1
        boats = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            boats += 1
        return boats

    def findNumbers(self, nums: list) -> int:
        count = 0
        res = 0
        s = []
        while sum(nums)!=0:
            nums =list(map(lambda x:x//10,nums))
            count += 1
            for i,j in enumerate(nums):
                if j ==0 and count %2==0 and i not in s:
                    res += 1
                if j == 0 :
                    s.append(i)

        return res

    def findNumbers1(self, nums: list) -> int:
        res = 0
        for i in nums:
            count = 0
            while i != 0:
                i//=10
                count +=1
            if count %2==0:
                res +=1

        return res

    def pushDominoes(self, dominoes: str) -> str:
        # 从左向右表示右倒的多米诺骨牌
        n = len(dominoes)
        right = [n]*n
        left = [n]*n
        j = 0
        count = n
        while j<n:

            if dominoes[j] == "R":
                count = 0
            elif dominoes[j] == '.' and count != n:
                count += 1
                right[j] = count
            else:
                count = n
            j += 1
        j = n-1
        count = n
        while j>=0:
            if dominoes[j] =='L':
                count = 0
            elif dominoes[j]=='.' and count !=n:
                count+=1
                left[j] = count
            else:
                count =n
            j-=1
        print(right)
        print(left)
        res = ''
        for i in range(n):
            if left[i]==right[i] and left[i]==n:
                res+=dominoes[i]
            elif left[i]==right[i] and left[i]!=n:
                res+='.'
            if left[i]<right[i]:
                res+='L'
            elif left[i]>right[i]:
                res+='R'
        return res

    def lengthOfLIS(self, nums: list) -> int:
        dp =[1] * len(nums)
        n = len(nums)
        for i in range(n):
            temp = 0
            for j in range(i):
                if nums[i]>nums[j] and dp[j] > temp:
                    temp = dp[j]
                    dp[i] = dp[j]+1
        return max(dp)
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        col = len(text1)
        row = len(text2)
        #dp = [[0]*(col+1)]*(row+1)
        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        for i in range(row):
            for j in range(col):
                temp = (1 if text2[i] == text1[j] else 0)
                dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j],dp[i][j]+temp)
        return dp[row][col]

    def minDistance(self, word1: str, word2: str) -> int:
        col = len(word1)
        row = len(word2)
        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        for i in range(row+1):
            dp[i][0] = i
        for j in range(col+1):
            dp[0][j] = j
        for i in range(row):
            for j in range(col):
                temp = (0 if word2[i] == word1[j] else 1)
                dp[i+1][j+1] = min(dp[i][j+1]+1,dp[i+1][j]+1,dp[i][j]+temp)
        return dp[row][col]


    def maxStudents(self, seats: list) -> int:

        def isSingleRowCompliant(status: int, row: int) -> bool:
            for j in range(n):
                if ((status >> j) & 1) == 1:
                    if seats[row][j] == '#':
                        return False
                    if j > 0 and ((status >> (j - 1)) & 1) == 1:
                        return False
            return True

        def isCrossRowsCompliant(status: int, upperRowStatus: int) -> bool:
            for j in range(n):
                if ((status >> j) & 1) == 1:
                    if j > 0 and ((upperRowStatus >> (j - 1)) & 1) == 1:
                        return False
                    if j < n - 1 and ((upperRowStatus >> (j + 1)) & 1) == 1:
                        return False
            return True

        @cache
        def dp(row: int, status: int) -> int:
            if not isSingleRowCompliant(status, row):
                return -inf
            students = bin(status).count('1')
            if row == 0:
                return students
            mx = 0
            for upperRowStatus in range(2 ** n):
                if isCrossRowsCompliant(status, upperRowStatus):
                    mx = max(mx, dp(row - 1, upperRowStatus))
            return students + mx

        m, n = len(seats), len(seats[0])
        mx = 0
        for i in range(2 ** n):
            mx = max(mx, dp(m - 1, i))
        return mx

    def minTimeToReach(self, moveTime: list) -> int:
        def dfs(arr:list,loc:list,i,j,flag):
            if i==0 and j==0:
                return
            # 定义四个方向
            dir = [[-1,0],[1,0],[0,-1],[0,1]]
            for q in range(len(dir)):
                dir[q][0] = dir[q][0] + i
                dir[q][1] = dir[q][1] + j
            minnum = 10000000000
            nexti = 0
            nextj = 0
            for n in range(len(dir)):
                x = dir[n][0]
                y = dir[n][1]
                if  x>= len(arr) or y >= len(arr[0]) or loc[x][y] == 1:
                    continue
                else:
                    if minnum>arr[x][y] + pow(2,flag%2):
                        nexti = x
                        nextj = y
                        minnum = arr[x][y] + pow(2,flag%2)

            loc[nexti][nextj] = 1
            arr[nexti][nextj] = minnum + arr[i][j]
            flag += 1
            dfs(arr,loc,nexti,nextj,flag)

        row = len(moveTime) - 1
        col = len(moveTime[0]) - 1
        moveTime[row][col] = 0
        loc = [[0 for i in range(col+1)] for j in range(row+1)]
        loc[row][col] = 1
        dfs(moveTime,loc,row,col,flag=0)
        return moveTime[0][0]



# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    G1 = [[0,20,inf,inf,inf,15,inf],[20,0,13,inf,inf,inf,inf],[inf,13,0,18,inf,inf,23],[inf,inf,18,0,7,inf,inf],[inf,inf,inf,7,0,26,inf],[15,inf,inf,inf,26,0,9],[inf,inf,23,inf,inf,9,0]]
    G2 = [[0,4,inf,inf,inf,inf,inf,8,inf],[4,0,8,inf,inf,inf,inf,11,inf],[inf,8,0,7,inf,4,inf,inf,2],[inf,inf,7,0,9,14,inf,inf,inf],[inf,inf,inf,9,0,10,inf,inf,inf],[inf,inf,4,14,10,0,2,inf,inf],[inf,inf,inf,inf,inf,2,0,1,6],[8,11,inf,inf,inf,inf,1,0,7],[inf,inf,2,inf,inf,inf,6,7,0]]
    G3 = [[0,20,inf,60,15],[inf,0,49,inf,inf],[inf,inf,0,inf,inf],[inf,inf,30,0,inf],[inf,inf,inf,48,0]]
    #s = Kruskal(G2,9)

    while not True:
        print("***")
    ss = Dijkstra(G3,0)
    #print(s.kruskal_work())
    print(ss.dijkstra_work())
