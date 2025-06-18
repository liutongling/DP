from collections import deque, Counter

from Dp import TreeNode


class EverDay:
    def __init__(self):
        #n皇后使用的变量
        self.n = 0
        self.mainLine =[]
        self.subLine = []
        self.col = []
        # n皇后使用的变量



    # 3337. 字符串转换后的长度 II
    def spin_char(self,char,num) ->str:
        charArr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        charIndex =ord(char ) -ord('a')
        charRes = ''
        while num!=0:
            charIndex += 1
            charIndex %= 26
            charRes += charArr[charIndex]
            num -= 1
        #print(charRes)
        return charRes
    # 这是使用模拟的方法，时间超时不能运行
    def lengthAfterTransformations0(self, s: str, t: int, nums: list) -> int:
        TempChar = s[:]
        while t!=0:
            Temp = TempChar[:]
            newChar = ''
            for i in Temp:
                newChar+=self.spin_char(i,nums[ord(i)-ord('a')])
            TempChar = newChar[:]
            t -= 1
        #print(TempChar)
        return len(TempChar)

    def lengthAfterTransformations(self, s: str, t: int, nums: list) -> int:
        sarr = []
        for i in s:
            sarr.append(ord(i))
        while t!=0:
            newarr = []
            for i in sarr:
                idx = (i - 97)%26
                idx1 = nums[idx]
                newarr.extend([i+j for j in range(1,idx1+1)])
            t -= 1
            sarr = newarr[:]
        return len(sarr)

    # 52. N 皇后 II

    def dfsQueens(self,row,n):
        if row == n:
            return 1
        count = 0
        for i in range(n):
            if self.col[i]==False and self.mainLine[i-row+n-1]==False and self.subLine[row+i]==False:
                self.col[i]=True
                self.mainLine[i-row+n-1] = True
                self.subLine[row+i]=True
                count+=self.dfsQueens(row+1,n)
                self.col[i]=False
                self.mainLine[i-row+n-1] = False
                self.subLine[row+i]=False
        return count



    def totalNQueens(self, n: int) -> int:

        self.mainLine = [False for _ in range(2*n-1)]
        self.subLine = [False for _ in range(2*n-1)]
        self.col = [False for _ in range(n)]
        # 存储主对角线上是否有皇后
        return self.dfsQueens(0,n)


    #78. 子集
    def subsets(self, nums: list) -> list:
        res = []
        opt = [0 for i in range(len(nums))]
        def dfs(nums:list,n,temp:list):
            if n == len(nums):
                res.append(temp[:])
                return
            opt[n] = 1
            temp.append(nums[n])
            dfs(nums,n+1,temp)
            temp.pop(-1)
            opt[n] = 0
            dfs(nums,n+1,temp)
            return res
        return dfs(nums, 0, [])
    # End**********************************
    #90. 子集 II
    def subsetsWithDup(self, nums: list) -> list:
        res = []
        opt = [0 for i in range(len(nums))]
        def dfs(nums:list,n,temp:list):
            if n == len(nums):
                res.append(temp[:])
                return
            opt[n] = 1
            temp.append(nums[n])
            if n>0 and opt[n-1] == 0 and nums[n] == nums[n-1]:
                pass
            else:dfs(nums,n+1,temp)
            opt[n] = 0
            temp.pop(-1)
            dfs(nums,n+1,temp)
        dfs(nums,0,[])
        return res
    # End**********************************

    #2900. 最长相邻不相等子序列 I
    def getLongestSubsequence0(self, words: list, groups: list) -> list:
        n = len(words)
        nums = [i for i in range(n)]
        res = self.subsets(nums)
        count = 0
        result = []
        for i in res:
            nn = len(i)
            if nn>count:
                flag = True
                for j in range(1,nn):
                    if groups[i[j-1]] == groups[i[j]]:
                        flag = False
                if flag == True:
                    count = nn
                    result = [words[k] for k in i]
        return result

    def getLongestSubsequence(self, words: list, groups: list) -> list:
        ans = []
        n = len(words)
        for i,g in enumerate(groups):
            if g!=groups[i+1] or i == n-1:
                ans.append(words[i])
        return ans

    # End**********************************
    #46. 全排列
    def permute(self, nums: list) -> list:
        n = len(nums)
        opt = [0 for _ in range(n)] # 标记是否被访问
        ans = [] # 存储结果
        def dfs_permute(nums:list,n,temp:list):
            if n == len(nums):# 如果访问到叶子节点则存储结果
                ans.append(temp[:]) # 这里要注意要复制list
            for i in range(len(nums)): # 遍历数组
                if opt[i] ==0: # 如果发现未被访问则进行递归
                    temp.append(nums[i]) # 将元素添加进去
                    opt[i] = 1 #标记已经被访问
                    dfs_permute(nums,n+1,temp) # 递归
                    opt[i] = 0 #回溯到上一个根节点的状态
                    temp.pop(-1) #回溯
        dfs_permute(nums, 0, [])
        return ans
    # End**********************************
    #全排列 II
    def permuteUnique(self, nums: list) -> list:
        ans = [] # 存储所有的结果
        opt = [0 for i in range(len(nums))] # 标记是否被访问
        nums.sort() # 必须要排序，这样方便判断上一个是否被访问
        def dfs(nums:list,n:int,temp:list):
            if n==len(nums):
                ans.append(temp[:])
                return
            ad = set()
            for i in range(len(nums)):
                if opt[i]==0 and nums[i] not in ad:
                    ad.add(nums[i])
                    opt[i] = 1
                    temp.append(nums[i])
                    dfs(nums,n+1,temp)
                    opt[i] = 0
                    temp.pop()
        dfs(nums,0,[])
        return ans

    # End**********************************
    #75. 颜色分类
    def sortColors(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums) - 1
        i = 0
        while i <= right:
            if nums[i] == 0 and i == left:
                left += 1
                i += 1
            elif nums[i] == 0 and i !=left:
                nums[i],nums[left] = nums[left],nums[i]
                left += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[i],nums[right] = nums[right],nums[i]
                right -= 1

    # End**********************************
    #361. 轰炸敌人
    def maxKilledEnemies(self, grid: list) -> int:
        m = len(grid)
        n = len(grid[0])
        dpRow = [[0 for _ in range(n)] for _ in range(m)]
        dpCol = [[0 for _ in range(n)] for _ in range(m)]
        # 这次遍历表示每行有多少敌人能够炸
        for i in range(m):
            pre = 0
            for j in range(n):
                if grid[i][j] == "E":
                    pre += 1
                elif grid[i][j] == "W":
                    pre = 0
                elif grid[i][j] =="0":
                    dpRow[i][j] += pre
            pre = 0
            for k in range(n-1,-1,-1):
                if grid[i][k] == "E":
                    pre += 1
                elif grid[i][k] == "W":
                    pre = 0
                elif grid[i][k] =="0":
                    dpRow[i][k] += pre
        for j in range(n):
            pre = 0
            for i in range(m):
                if grid[i][j] == "E":
                    pre += 1
                elif grid[i][j] == "W":
                    pre = 0
                elif grid[i][j] =="0":
                    dpCol[i][j] += pre
            pre = 0
            for k in range(m-1,-1,-1):
                if grid[k][j] == "E":
                    pre += 1
                elif grid[k][j] == "W":
                    pre = 0
                elif grid[k][j] =="0":
                    dpCol[k][j] += pre
        res = 0
        for i in range(m):
            for j in range(n):
                temp = dpRow[i][j]+ dpCol[i][j]
                if res < temp:
                    res = temp
        return res

    # End**********************************


    def triangleType(self, nums: list) -> str:
        a = nums[0]
        b = nums[1]
        c = nums[2]
        if a > b:
            a , b = b , a
        if a > c:
            a , c = c , a
        if c < b:
            c , b = b ,c
        if c < a + b:
            if a == b and a == c:
                return "equilateral"
            if a==b or b == c:
                return "isosceles"
            if a != b and b!=c:
                return "scalene"
        else:
            return "none"

    # 3355.零数组变换I
    def isZeroArray0(self, nums: list, queries: list) -> bool:
        hashTable = {}
        for i in queries:
            for j in range(i[0],i[-1]+1):
                if j not in hashTable.keys():
                    hashTable[j] = 1
                else:hashTable[j] += 1
        flag = True
        for i,value in enumerate(nums):
            if i not in hashTable.keys():
                if value !=0:
                    flag = False
                    break
            elif hashTable[i] < value:
                flag = False
                break
        return flag

    def isZeroArray(self, nums: list, queries: list) -> bool:
        dil = [0 for i in range(len(nums)+1)]
        for i in queries:
            dil[i[0]] += 1
            dil[i[1]+1] -= 1
        addSum = 0
        flag = True
        for i , value in enumerate(nums):
            addSum += dil[i]
            if addSum < value:
                flag = False
                break
        return flag

    # End**********************************
    # 3356.零数组变换II

    def minZeroArray(self, nums: list, queries: list) -> int:# 未解决，超时不能解决，需要用到二分查找，思路是第k满足那么第k+1也满足，这个条件就可以使用二分查找
        dil = [0] * (len(nums)+1)
        for idx,i in enumerate(queries):
            dil[i[0]] += i[2]
            dil[i[1]+1] -= i[2]
            for j in range(i[0],i[1]+1):
                if nums[j] > 0:
                    if nums[j] > i[2]:
                        nums[j] -= i[2]
                    else:
                        nums[j] = 0
            if sum(nums) == 0:
                return idx+1
        return -1
    # End**********************************
    # 广度优先搜索

    def bfs(self, root:TreeNode) -> int:
        #定义一个队列
        que = [] # 这里直接就用一个列表表示
        que.append(root)
        while len(que) != 0:#判断是否为空
            # 弹出队首元素
            temp = que.pop(0)
            if temp.left != None: # 如果左节点不空，加入到队列中
                que.append(temp.left)
            if temp.right !=None: # 如果右节点不空，加入到队列中
                que.append(temp.right)

    # End**********************************

    # 3372.连接两棵树后最大目标节点数目I
    
    def maxTargetNodes(self, edges1: list, edges2: list, k: int) -> list:
        # 定义找到第一树点的所有节

        return

    # End**********************************

    # 3372.连接两棵树后最大目标节点数目I
    def closestMeetingNode1(self, edges: list, node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        rootNode1 = {}
        rootNode2 = {}
        temp = node1
        i = 0
        rootNode1[temp] = 0
        while edges[temp] != -1 and (edges[temp] not in rootNode1.keys()):
            i += 1
            rootNode1[edges[temp]] = i
            temp = edges[temp]
        temp = node2
        i = 0
        rootNode2[temp] =0
        while edges[temp] != -1 and (edges[temp] not in rootNode2.keys()):
            i += 1
            rootNode2[edges[temp]] = i
            temp = edges[temp]
        res = -1
        restemp = len(edges)
        for i in rootNode1.keys():
            if i in rootNode2.keys():
                if restemp > max(rootNode2[i],rootNode1[i]):
                    restemp = max(rootNode2[i],rootNode1[i])
                    res = i
        return res
    def closestMeetingNode2(self, edges: list, node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        rootNode1 = {}
        rootNode2 = {}
        temp = node1
        i = 0
        rootNode1[temp] = 0
        while edges[temp] != -1 and (edges[temp] not in rootNode1.keys()):
            i += 1
            rootNode1[edges[temp]] = i
            temp = edges[temp]
        temp = node2
        i = 0
        rootNode2[temp] =0
        while edges[temp] != -1 and (edges[temp] not in rootNode2.keys()):
            i += 1
            rootNode2[edges[temp]] = i
            temp = edges[temp]
        res = max(edges) + 1
        restemp = len(edges)
        for i in rootNode1.keys():
            if i in rootNode2.keys():
                if restemp >= max(rootNode2[i],rootNode1[i]):
                    if restemp == max(rootNode2[i],rootNode1[i]):
                        res = i if res > i else res
                    restemp = max(rootNode2[i],rootNode1[i])
                    res = i
        return -1 if res == max(edges)+1 else res

    def closestMeetingNode(self, edges: list, node1: int, node2: int) -> int:
        if node1 == node2:
            return node1
        rootNode1 = {}
        rootNode2 = {}
        temp = node1
        i = 0
        rootNode1[temp] = 0
        while edges[temp] != -1 and (edges[temp] not in rootNode1.keys()):
            i += 1
            rootNode1[edges[temp]] = i
            temp = edges[temp]
        temp = node2
        i = 0
        rootNode2[temp] = 0
        while edges[temp] != -1 and (edges[temp] not in rootNode2.keys()):
            i += 1
            rootNode2[edges[temp]] = i
            temp = edges[temp]
        res = max(edges) + 1
        restemp = len(edges)
        for i in rootNode1.keys():
            if i in rootNode2.keys():
                distance = max(rootNode2[i], rootNode1[i])
                if restemp >= distance:
                    if restemp == distance:
                        res = i if res > i else res
                    else:
                        res = i
                        restemp = distance
        return -1 if res == max(edges) + 1 else res
    # End**********************************
    def robotWithString(self, s: str) -> str:
        n = len(s)
        tempchar = [s[n-1] for _ in range(n)]
        for i in range(n-2,-1,-1):
            if ord(s[i]) < ord(tempchar[i+1]):
                tempchar[i] = s[i]
            else:
                tempchar[i] = tempchar[i+1]
        stack = []

        que = tempchar[:]
        result = ""
        for i in range(n):
            if ord(s[i]) > ord(tempchar[i]):
                stack.append(s[i])
                que.pop(0)
            elif ord(s[i]) == ord(tempchar[i]):
                stack.append(s[i])
                tempca = que[0]
                while len(stack) > 0 and ord(stack[-1]) <= ord(tempca):
                    result += stack.pop(-1)
                    if len(que)>0 and que[0] ==s[i] :que.pop(0)
        print(result)
        return result

    # 386.字典序排数
    def lexicalOrder(self, n: int) -> list:
        arrNums = [str(i) for i in range(1, n+1)]
        arrNums.sort()
        res = []
        for i in range(n):
            res.append(int(arrNums[i]))
        # print("hello world")
        # print(res)
        return res
    # End**********************************
    # 50.pow函数
    def myPow(self, x: float, n: int) -> float:
        if n==1:
            return x
        if n == 0:
            return 1
        temp = n%2
        return self.myPow(x,n//2) *self.myPow(x,n//2+temp)

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        half = self.myPow(x, n // 2)  # 计算一次子问题
        if n % 2 == 0:
            return half * half
        else:
            return half * half * x  # 奇数时补乘x
    # End**********************************
    # 3442.奇偶频次最大值I
    def maxDifference(self, s: str) -> int:
        count = [0]*26
        for i in s:
            count[ord(i)-97]+=1
        countj = 0
        counto = len(s)
        for j in range(26):
            if count[j] == 0:
                continue
            if count[j] %2 ==0 and count[j]<counto :
                counto = count[j]
            if count[j] %2 ==1 and count[j]>countj:
                countj = count[j]

        return countj - counto

    # End**********************************
    def maximumDifference(self, nums: list) -> int:
        maxSub = -1
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[j] != nums[i]:
                    tempSub = nums[j] - nums[i]
                    if maxSub < tempSub:
                        maxSub = tempSub
        return maxSub

    # 209 第一个唯一数字
    def minSubArrayLen(self, target: int, nums: list) -> int:
        n = len(nums)
        maxnum = n
        temp = 0
        for i in range(n):
            tempSum = 0
            for j in range(i, n):
                tempSum += nums[j]
                if tempSum >= target and (j-i+1)<maxnum:
                    maxnum = (j-i+1)
                    temp = tempSum
                    break
        return maxnum if temp>=target else 0
    # End**********************************

# 1429 第一个唯一数字
class FirstUnique:
    def __init__(self, nums: list):
        self.HelpDueue = deque(nums)
        self.HelpDict = Counter(nums)

    def showFirstUnique(self) -> int:
        while self.HelpDueue and self.HelpDict[self.HelpDueue[0]]>1:
            self.HelpDueue.popleft()
        if self.HelpDueue:
            return self.HelpDueue[0]
        return -1
    def add(self, value: int) -> None:
        self.HelpDict[value]+=1
        self.HelpDueue.append(value)


