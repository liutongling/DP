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
