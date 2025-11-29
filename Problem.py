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

