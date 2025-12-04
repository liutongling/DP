from queue import PriorityQueue
class EveryDayLeetCode:
    def numberOfPaths(self, grid: list, k: int) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                grid[i][j] = grid[i][j] % k

        def dfs(i,j,pre):
            if i<0 or j<0:
                return 0
            pre = (grid[i][j]+pre)%k
            if i==0 and j==0:
                return 1 if pre==0 else 0
            return (dfs(i-1,j,pre) + dfs(i,j-1,pre))%(10**9+7)
        return dfs(len(grid)-1,len(grid[0])-1,0)
    def combine(self, n: int, k: int) -> list:
        result = []
        def dfs(n:int,t,lev:int,tempList:list):
            if lev==k:
                result.append(tempList[:])
                return
            for i in range(t,n+1):
                if  (n-i)>=(k-lev -1):
                    tempList.append(i)
                    #remark[i] = 1
                    dfs(n,i+1,lev+1,tempList)
                    tempList.pop()
                    #remark[i] = 0

        dfs(n,1,0,[])
        print(result)
        return result

    def findTargetSumWays(self, nums: list, target: int) -> int:
        # 使用回溯的方法求解
        def dfs(nums:list,lev,sum1,sum2,target:int):
            if lev==len(nums):
                if sum1+sum2==target:
                    return 1
                else:
                    return 0
            else:
                l = dfs(nums,lev+1,sum1+nums[lev],sum2,target)
                r = dfs(nums,lev+1,sum1,sum2-nums[lev],target)
                return l+r
        return dfs(nums,0,0,0,target)
    #2141 同时运行n台电脑
    def maxRunTime(self, n: int, batteries: list) -> int:
        que = PriorityQueue(batteries)
        return 0

