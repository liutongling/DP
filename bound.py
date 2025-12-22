import heapq
import sys

from fontTools.ttLib.ttVisitor import visit

from Dp import TreeNode


class BoundTest:
    def bfs(self,root:TreeNode):
        que = [root]
        dil = 10
        while len(que) != 0:
            temp = que.pop(0)
            if temp.left != None and temp.left.val>dil:
                que.append(temp.left)
            if temp.right != None and temp.right.val >dil:
                que.append(temp.right)
            print(temp.val)



class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value / weight  # 价值重量比

    def __lt__(self, other):
        return self.ratio > other.ratio  # 为了最大堆，按比例降序排列


class Node:
    def __init__(self, level, profit, weight, bound, items):
        self.level = level  # 树的层级（决策到第几个物品）
        self.profit = profit  # 当前节点的总价值
        self.weight = weight  # 当前节点的总重量
        self.bound = bound  # 价值上界
        self.items = items  # 选择的物品列表

    def __lt__(self, other):
        # 为了最大堆，按bound降序排列
        return self.bound > other.bound

# 参数分别表示node:当前的节点,capacity:剩余容量，items:表示存储各个物品的价值和质量，n:表示总共有几个物品
def bound(node, capacity, items, n):
    # 如果重量超过容量，直接返回0（不可能有更优解）
    if node.weight >= capacity:
        return 0

    # 初始化上界为当前价值
    profit_bound = node.profit
    total_weight = node.weight
    j = node.level + 1

    # 贪心地添加物品，直到不能再添加为止
    while j < n and total_weight + items[j].weight <= capacity:
        total_weight += items[j].weight
        profit_bound += items[j].value
        j += 1

    # 如果还有剩余物品，添加一部分以计算上界
    if j < n:
        profit_bound += (capacity - total_weight) * items[j].ratio

    return profit_bound


def branch_and_bound_knapsack(capacity, weights, values, n):
    # 创建物品列表并按价值重量比排序
    items = [Item(weights[i], values[i]) for i in range(n)]
    items.sort()  # 按价值重量比降序排列

    # 初始化最大堆
    max_heap = []

    # 创建根节点（未选择任何物品）
    root = Node(-1, 0, 0, 0, [])
    root.bound = bound(root, capacity, items, n)

    heapq.heappush(max_heap, root)

    max_profit = 0
    best_items = []

    while max_heap:
        # 取出bound最大的节点
        current_node = heapq.heappop(max_heap)

        # 如果当前节点的bound小于已知最大profit，则剪枝
        if current_node.bound < max_profit:
            continue

        # 如果已经到达叶子节点，更新最大值
        if current_node.level == n - 1:
            continue

        # 处理左子节点（选择下一个物品）
        next_level = current_node.level + 1
        left_weight = current_node.weight + items[next_level].weight
        left_profit = current_node.profit + items[next_level].value
        left_items = current_node.items.copy() #该层选择哪些物品拷贝过来
        left_items.append(next_level) # 将该物品加入候选单中

        # 如果重量不超过容量且价值更大，更新最大值
        if left_weight <= capacity and left_profit > max_profit:
            max_profit = left_profit
            best_items = left_items.copy()

        # 计算左子节点的bound
        left_bound = bound(Node(next_level, left_profit, left_weight, 0, left_items),
                           capacity, items, n)

        # 如果bound大于当前最大profit，则加入堆
        if left_bound > max_profit:
            left_node = Node(next_level, left_profit, left_weight, left_bound, left_items)
            max_heap.append(left_node)

        # 处理右子节点（不选择下一个物品）
        right_bound = bound(Node(next_level, current_node.profit, current_node.weight, 0, current_node.items),
                            capacity, items, n)

        # 如果bound大于当前最大profit，则加入堆
        if right_bound > max_profit:
            right_node = Node(next_level, current_node.profit, current_node.weight, right_bound, current_node.items)
            max_heap.append(right_node)


    # 返回最大价值和选择的物品索引
    return max_profit, best_items



# 单调队列实现
def branch_and_bound_knapsack1(capacity, weights, values, n):
    # 创建物品列表并按价值重量比排序
    items = [Item(weights[i], values[i]) for i in range(n)]
    items.sort()  # 按价值重量比降序排列
    # 初始化最大堆
    max_heap = []
    # 创建根节点（未选择任何物品）
    root = Node(-1, 0, 0, 0, [])
    root.bound = bound(root, capacity, items, n)
    max_heap.append(root)
    max_profit = 0
    best_items = []
    while max_heap:
        node = max_heap.pop(0)
        if node.bound < max_profit:
            continue
        # 如果节点，因为层次从-1开始，n-1的节点已经是叶子节点
        if node.level == n - 1:
            continue
        # 处理左节点
        left_level = node.level + 1
        left_weight = node.weight + items[left_level].weight
        left_profit = node.profit + items[left_level].value
        left_items = node.items.copy()
        left_items.append(left_level)

        if left_weight <= capacity and left_profit > max_profit:
            max_profit = left_profit
            best_items = left_items.copy()
        left_node = Node(left_level, left_profit, left_weight, 0,left_items)
        left_bound = bound(left_node, capacity, items, n)
        if left_bound > max_profit:
            left_node.bound = left_bound
            max_heap.append(left_node)


        right_node = Node(node.level+1, node.profit, node.weight, 0, node.items)
        right_bound = bound(right_node, capacity, items, n)

        if right_bound > max_profit:
            right_node.bound = right_bound
            max_heap.append(right_node)
    return max_profit, best_items

# 示例使用
    #(1)
    # capacity = 5
    # weights = [2,4,5,3]
    # values = [12,16,15,6]
    # n = len(values)
    #(2)
    # capacity = 5
    # weights = [1,2,3]
    # values = [3,3.2,3.3]
    # n = len(values)
    # (3)
    # capacity = 10
    # weights = [4, 7, 5, 3]
    # values = [40, 42, 25, 12]
    # n = len(values)
    #
    # max_profit, selected_items = branch_and_bound_knapsack(capacity, weights, values, n)
    #
    # print("最大价值:", max_profit)
    # print("选择的物品索引:", selected_items)
    # print("对应的重量:", [weights[i] for i in selected_items])
    # print("对应的价值:", [values[i] for i in selected_items])




# 任务分配问题
class Task:
    def __init__(self,v:int,lb:int,lev:int,res:list,target:int,visited:list):
        self.v = v # 当前节点的价值
        self.lb = lb # 通过限界函数计算的最小值 ，下限
        self.lev = lev # 当前层
        self.res = res # 解向量
        self.target = target # 当前目标值的上限，可能的解
        self.visited = visited # 当前拜访的列节点（标记任务是否被访问）
    def __lt__(self, other):
        return self.lb < other.lb # 根据lb计算优先级



# 当是根节点的时候，可以通过贪心算法算出该问题的上界和下界
def get_bound(Node:Task,task:list):# 找根节点的下界，只需要找到每个人员完成任务的最小值即可
    down = Node.v
    lev = Node.lev
    n = len(task)
    for i in range(lev+1,n):
        temp = task[i][0]
        for j in range(n):
            if task[i][j] < temp:# 每次获取最小值，得到下限
                temp = task[i][j]
        down += temp
    return down

def get_target(Node:Task,task:list): #此时需要利用贪心算法求上界，该上界需要满足每个员工都有任务
    n = len(task)
    down = Node.v
    lev = Node.lev
    vis = Node.visited.copy()
    for i in range(lev+1,n):
        temp = sys.maxsize
        fl = 0
        for j in range(n):
            if task[i][j] < temp and vis[j] == 0:
                fl = j
                temp = task[i][j]
        vis[fl] = 1
        down += temp
    return down

def mission_problem(task:list):
    n = len(task)

    myheap = []
    root = Task(0,0,-1,[],0,[0,0,0,0])
    heapq.heappush(myheap,root)

    # 保存当前目标函数的最优值
    min_profit = get_target(root,task)
    best_items = root.res
    root.lb = get_bound(root,task)
    while myheap:
        node = heapq.heappop(myheap)
        if node.lev == n - 1: # 如果是最后的叶子节点直接出队
            continue
        # 通过让node出队，然后产生所有子节点，然后判断这些节点是否入队
        for i in range(n):
            if node.visited[i] == 0:
                next_lev = node.lev + 1
                next_v = node.v + task[next_lev][i]
                next_lb = 0
                next_res = node.res.copy()
                next_res.append(i)
                next_target = 0
                next_visited = node.visited.copy()
                next_visited[i] = 1
                temp = Task(next_v,next_lb,next_lev,next_res,next_target,next_visited)
                temp.lb = get_bound(temp,task)
                temp.target = get_target(temp,task)
                # 目标值的更新
                if temp.target < min_profit:
                    min_profit = temp.target
                # 下限界函数满足条件就入队
                if temp.lb <= min_profit:
                    min_profit = temp.target
                    heapq.heappush(myheap,temp)
                    if temp.target == min_profit:
                        best_items = temp.res.copy()
    print(min_profit)
    print(best_items)
    return min_profit,best_items



