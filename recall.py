# 使用回溯算法解决背包问题
class Recall:
    def canPartition1(self, nums: list) -> bool:
        def dfs(nums, level, sum1, sum2):
            if level == len(nums) and sum1 == sum2:
                return True
            elif level == len(nums) and sum1 != sum2:
                return False

            l = dfs(nums, level + 1, sum1 + nums[level], sum2)

            r = dfs(nums, level + 1, sum1, sum2 + nums[level])
            return l or r
        return dfs(nums,0,0,0)

    # 101.分割等和子集
    # 给定一个非空的正整数数组 nums ，请判断能否将这些数字分成元素和相等的两部分
    def canPartition(self, nums: list) -> bool:
        if sum(nums) % 2 == 1:
            return False
        V = sum(nums) // 2
        dp = [False] * (V+1)
        dp[0] = True
        for i in range(1, len(nums)+1):
            for j in range(V, 0, -1):
                if nums[i -1] <= j:
                    dp[j] = dp[j] or dp[j-nums[i-1]]
                #print(j)
            print(dp)
        return dp[-1]

    # 77.给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。可以按 任何顺序 返回答案。
    # 示例输入：n = 4, k = 2 输出：
    # [
    #   [2,4],
    #   [3,4],
    #   [2,3],
    #   [1,2],
    #   [1,3],
    #   [1,4],
    # ]
    def combine(self, n: int, k: int) -> list:
        result = []

        def dfs(n: int, t, lev: int, tempList: list):
            if lev == k:
                result.append(tempList[:])
                return
            for i in range(t, n + 1):
                if (n - i) >= (k - lev - 1):
                    tempList.append(i)
                    dfs(n, i + 1, lev + 1, tempList)
                    tempList.pop()


        dfs(n, 1, 0, [])
        # print(result)
        return result
    # 全排列I 该问题还可以解的方法1.头中尾插入法、2.抽丝法、3.交换法、4、前缀法 (Prefix Method)
    # 1. 头中尾插入法 (Insertion Method)
    # 思路：
    # 对于n个元素的全排列，可以看作在n-1个元素全排列的基础上，将第n个元素插入到每个排列的各个位置
    #
    # 例如：对于[1,2,3]，先得到[1,2]的排列：[1,2], [2,1]
    #
    # 然后将3插入每个排列的每个位置：头、中、尾
    def permute(self, nums: list) -> list:
        result = []

        def dfs(nums: list,Visit:list, lev: int, TempList: list):

            if lev == len(nums):
                result.append(TempList[:])
                return
            for i in range(len(nums)):
                if Visit[i]==0:
                    Visit[i] = 1
                    TempList.append(nums[i])
                    dfs(nums,Visit,lev,TempList)
                    Visit[i] = 0
                    TempList.pop()
        return result
    # switch method
    def permute_switch(self, nums: list) -> list:
        result = []

        def dfs(start:int):
            if start == len(nums):
                result.append(nums[:])
                print(nums)
                return
            for i in range(start,len(nums)):
                nums[start] , nums[i] = nums[i], nums[start]
                dfs(start+1)
                nums[i] , nums[start] = nums[start], nums[i]

        dfs(0)
        return result

    def subsets(self, nums: list) -> list:
        result = []
        def dfs(start:int ,Temp:list):
            if start == len(nums):
                result.append(Temp[:])
                return
            Temp.append(nums[start])
            dfs(start+1,Temp)
            Temp.pop()
            dfs(start + 1, Temp)
        dfs(0,[])
        print(result)

        return result
