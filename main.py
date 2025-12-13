
import heapq

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
# def bound(node, capacity, items, n):
#     # 如果重量超过容量，直接返回0（不可能有更优解）
#     if node.weight >= capacity:
#         return 0
#
#     # 初始化上界为当前价值
#     profit_bound = node.profit
#     total_weight = node.weight
#     j = node.level + 1
#
#     # 贪心地添加物品，直到不能再添加为止
#     while j < n and total_weight + items[j].weight <= capacity:
#         total_weight += items[j].weight
#         profit_bound += items[j].value
#         j += 1
#
#     # 如果还有剩余物品，添加一部分以计算上界
#     if j < n:
#         profit_bound += (capacity - total_weight) * items[j].ratio
#
#     return profit_bound
def bound(node, capacity, items, n):
    # 如果重量超过容量，直接返回0（不可能有更优解）
    if node.weight >= capacity:
        return 0

    j = node.level+1
    if j >= n:
        return 0
    profit_bound = node.profit
    profit_bound+=  ((capacity-node.weight)*items[j].ratio)

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
            heapq.heappush(max_heap, left_node)

        # 处理右子节点（不选择下一个物品）
        right_bound = bound(Node(next_level, current_node.profit, current_node.weight, 0, current_node.items),
                            capacity, items, n)

        # 如果bound大于当前最大profit，则加入堆
        if right_bound > max_profit:
            right_node = Node(next_level, current_node.profit, current_node.weight, right_bound, current_node.items)
            heapq.heappush(max_heap, right_node)

    # 返回最大价值和选择的物品索引
    return max_profit, best_items






if __name__ == '__main__':
    # G = [[0, 20, math.inf, math.inf, math.inf, 15, math.inf],
    #      [20, 0, 13, math.inf, math.inf, math.inf, math.inf],
    #      [math.inf, 13, 0, 18, math.inf, math.inf, 23],
    #      [math.inf, math.inf, 18, 0, 7, math.inf, math.inf],
    #      [math.inf, math.inf, math.inf, 7, 0, 26, math.inf],
    #      [15, math.inf, math.inf, math.inf, 26, 0, 9],
    #      [math.inf, math.inf, 23, math.inf, math.inf, 9, 0],
    #      ]
    # G = [[0, 1, math.inf, math.inf, math.inf, 1, math.inf],
    #      [1, 0, 1, math.inf, math.inf, math.inf, math.inf],
    #      [math.inf, 1, 0, 20, math.inf, math.inf, 1],
    #      [math.inf, math.inf, 20, 0, 20, math.inf, math.inf],
    #      [math.inf, math.inf, math.inf, 20, 0, 20, math.inf],
    #      [1, math.inf, math.inf, math.inf, 20, 0, 1],
    #      [math.inf, math.inf, 1, math.inf, math.inf, 1, 0],
    #      ]
    # M = 7
    # primTest = Prim(M,G)
    # result = primTest.prim_work()
    # print(result)

    # g = Dijkstra1(5)
    # g.add_edge(0, 1, 20)
    # g.add_edge(0, 3, 60)
    # g.add_edge(0, 4, 15)
    # g.add_edge(1, 2, 42)
    # g.add_edge(3, 2, 30)
    # g.add_edge(4, 3, 23)
    #
    # g.dijkstra_work(0)

    # s=Solution()
    # r =  s.lengthOfLIS([0,1,0,3,2,3])# tower_math([[2],[6,9],[8,2,0],[4,6,7,3],[6,5,2,1,5]])
    # print(r)
    # s = Solution()
    # s.maximalSquare([["0","1"],["1","0"]])
    #res = bag0_1([2,3,4,7],[1,3,5,9],V=10)
    #print(res)

    # solution = EveryDayLeetCode()
    # solution.combine(4,4)
    # print(math.ceil(0.1))
    # TestPass([0.6, 0.6, 0.6])
    # print("*****************")
    # pass_probability(3,[0.6, 0.6, 0.6])
    # sts = [0]
    # s = Recall()
    # s.subsets_bit([1,2,3])

    capacity = 10
    weights = [2,4,5,3]
    values = [12,16,15,6]
    n = len(values)

    max_profit, selected_items = branch_and_bound_knapsack(capacity, weights, values, n)

    print("最大价值:", max_profit)
    print("选择的物品索引:", selected_items)
    print("对应的重量:", [weights[i] for i in selected_items])
    print("对应的价值:", [values[i] for i in selected_items])