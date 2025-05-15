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

    def permute(self, nums: list) -> list:
        n = len(nums)
        opt = [0 for _ in range(n)]
        ans = []
        def dfs_permute(nums:list,n,temp:list):
            if n == len(nums):
                ans.append(temp[:])
            for i in range(len(nums)):
                if opt[i] ==0:
                    temp.append(nums[i])
                    opt[i] = 1
                    dfs_permute(nums,n+1,temp)
                    opt[i] = 0
                    temp.pop(-1)
        dfs_permute(nums, 0, [])
        return ans
