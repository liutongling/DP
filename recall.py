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
    def subsets_bit(self, nums: list) -> list:
        result = []
        for i in range(pow(2, len(nums))):
            temp = []
            for j in range(len(nums)):
                if (i&(1<<j))!=0:
                    temp.append(nums[j])
            result.append(temp[:])
        print(result)
        return result

    #n皇后 问题
    def solveNQueens(self, n: int) -> list:
        col = [0]*n
        main_Line = [0]*(2*n-1)
        sub_Line = [0]*(2*n-1)
        def dfs(n:int,lev:int,temp:list)->int:
            if n==lev:

                return 1
            count = 0
            for i in range(n):
                if col[i]==0 and main_Line[i+lev]==0 and sub_Line[i-lev+n-1]==0:
                    col[i] = 1
                    main_Line[i+lev] = 1
                    sub_Line[i-lev+n-1] = 1
                    count+=dfs(n,lev+1)
                    col[i] = 0
                    main_Line[i+lev] = 0
                    sub_Line[i-lev+n-1] = 0
            return count
        return dfs(n,0,)

    #用回溯求解0-1背包问题
    def recallKnap(self,w:list,v:list,C:int)->int:
        n = len(w)
        def dfs(lev:int,wi:int,val:int)->int:
            if lev==n:
                return val
            # 对该物品进行选择
            leftv = 0
            rightv = 0
            if wi+w[lev] < C:
                leftv = dfs(lev+1,wi+w[lev],val+v[lev])
            #对该物品不选择
            rightv = dfs(lev+1,wi,val)

            return max(leftv,rightv)
        return dfs(0,0,0)

def find_Path(pic:list,s:list,e:list)->int:
    #定义四个方向 向右，向下   向左，  向上
    pic[s[0]][s[1]] = 1
    direct = [[0,1],[1,0],[0,-1],[-1,0]]
    def dfs(x:int,y:int,)->int:
        if x==e[0] and y==e[1]:
            return 1
        count = 0
        for dx,dy in direct:
            x1,y1 = x+dx, y+dy
            if pic[x1][y1] ==0:
                pic[x1][y1] = 1
                count += dfs(x1,y1)
                pic[x1][y1] = 0
        return count
    return dfs(s[0],s[1])
def find_Path1(pic: list, s: list, e: list) -> int:
    # 深拷贝迷宫
    temp = [row[:] for row in pic]
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    rows = len(temp)
    cols = len(temp[0])

    def dfs(x: int, y: int) -> int:
        if x == e[0] and y == e[1]:
            return 1
        count = 0
        for dx, dy in direct:
            x1, y1 = x + dx, y + dy
            # 边界检查且为可通过
            if 0 <= x1 < rows and 0 <= y1 < cols and temp[x1][y1] == 0:
                temp[x1][y1] = 1
                count += dfs(x1, y1)
                temp[x1][y1] = 0
        return count

    # 标记起点为已访问
    temp[s[0]][s[1]] = 1
    return dfs(s[0], s[1])


def find_paths(maze, start, end):
    """
    计算从起点到终点的所有路径数量

    参数:
    maze: 二维列表，0表示可通过，1表示墙
    start: 起点坐标 (行, 列)
    end: 终点坐标 (行, 列)

    返回:
    路径数量
    """
    # 深拷贝迷宫，避免修改原数据
    temp = [row[:] for row in maze]

    # 方向：右、下、左、上
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    rows = len(temp)
    cols = len(temp[0])

    # 检查坐标是否在迷宫内且可通过
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols and temp[x][y] == 0

    def dfs(x, y):
        # 到达终点，找到一条路径
        if x == end[0] and y == end[1]:
            return 1

        total_paths = 0
        # 标记当前位置为已访问
        temp[x][y] = 1

        # 尝试四个方向
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y):
                total_paths += dfs(new_x, new_y)

        # 回溯：恢复当前位置为未访问
        temp[x][y] = 0

        return total_paths

    # 确保起点和终点可通过
    if (temp[start[0]][start[1]] == 1 or
            temp[end[0]][end[1]] == 1):
        return 0

    # 从起点开始搜索
    return dfs(start[0], start[1])


def is_valid_color(node, color, graph, colors):
   for neighbor in range(len(graph)):
       if graph[node][neighbor] == 1 and colors[neighbor] == color:
           return False
   return True
def graph_coloring(graph, m_colors, colors, node):
   if node == len(graph):
       return True # 所有节点已成功着色
   for color in range(1, m_colors + 1):
       if is_valid_color(node, color, graph, colors):
           colors[node] = color
           if graph_coloring(graph, m_colors, colors, node + 1):
               return True
           colors[node] = 0 # 回溯
   return False
# 示例输入
graph = [
   [0, 1, 1, 1],
   [1, 0, 1, 0],
   [1, 1, 0, 1],
   [1, 0, 1, 0]
]
m_colors = 3
colors = [0] * len(graph)
if graph_coloring(graph, m_colors, colors, 0):
   print("找到一种可行的着色方案:", colors)
else:
   print("无法找到可行的着色方案")