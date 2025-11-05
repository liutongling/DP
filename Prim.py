import math
from queue import PriorityQueue

# 定义一个优先队列

class Prim:
    def __init__(self,M,G:list):
        # 初始化图
        self.g = G # G是一个邻接矩阵，M是有多少个节点
        #存储最小生成树的点集
        self.point = set([i for i in range(M)]) # 初始化多少个节点
        self.setPath = [] #没有用到
        self.setPoint = set() # 用来保存添加之后的节点
        self.res = set() # 没有用到

    def prim_work(self):
        pq = PriorityQueue()
        pq.put((0,0)) # 初始化节点
        disAll = 0 # 保存最小生成树的总边长
        while not ((self.setPoint&self.point)==self.point):
            next = pq.get() # 弹出最小边
            nextP = next[1] # 下一个节点
            if nextP not in self.setPoint:
                self.setPoint.add(nextP)
                disAll+=next[0]
                print(nextP,next[0])
            # self.res.add(next)
            for j in range(len(self.g[nextP])):
                dis = self.g[nextP][j]
                if dis != math.inf and j not in self.setPoint:
                    pq.put((dis,j))

        return disAll

# if __name__ == '__main__':
#     G = [[0, 20, math.inf, math.inf, math.inf, 15, math.inf],
#          [20, 0, 13, math.inf, math.inf, math.inf, math.inf],
#          [math.inf, 13, 0, 18, math.inf, math.inf, 23],
#          [math.inf, math.inf, 18, 0, 7, math.inf, math.inf],
#          [math.inf, math.inf, math.inf, 7, 0, 26, math.inf],
#          [15, math.inf, math.inf, math.inf, 26, 0, 9],
#          [math.inf, math.inf, 23, math.inf, math.inf, 9, 0],
#          ]
#     M = 7
#     primTest = Prim(M,G)
#     result = primTest.prim_work()
#     print(result)
import heapq


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        # 邻接表，每个顶点存储 (邻居节点, 权重) 列表
        self.adj = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.adj[u].append((v, w))
        self.adj[v].append((u, w))  # 无向图，两个方向都加


def prim_mst(graph):
    V = graph.V
    visited = [False] * V
    min_heap = [(0, 0)]  # (权重, 节点)，从节点0开始
    mst_weight = 0
    mst_edges = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += weight

        # 若不是起点，记录MST边信息
        if weight != 0:
            mst_edges.append((u, weight))

        for v, w in graph.adj[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    if all(visited):
        return mst_weight, mst_edges
    else:
        return None  # 图不连通时返回 None


# 使用示例
# if __name__ == "__main__":
#     g = Graph(5)
#     g.add_edge(0, 1, 2)
#     g.add_edge(0, 3, 6)
#     g.add_edge(1, 2, 3)
#     g.add_edge(1, 3, 8)
#     g.add_edge(1, 4, 5)
#     g.add_edge(2, 4, 7)
#     g.add_edge(3, 4, 9)
#
#     total_weight, mst_edges = prim_mst(g)
#     print(f"MST 总权重: {total_weight}")
#     print("MST 边组成:")
#     for edge in mst_edges:
#         print(edge)
# Python 实现 Prim 算法 - 基于邻接矩阵

import sys

def prim_for(graph):
    num_vertices = len(graph)
    selected = [False] * num_vertices  # 标记节点是否已加入 MST
    # 用于存储 MST 的边
    mst_edges = []

    # 初始化，从第一个节点开始
    selected[0] = True
    edge_count = 0

    while edge_count < num_vertices - 1:
        min_weight = sys.maxsize
        u = v = -1

        # 遍历已加入 MST 的节点
        for i in range(num_vertices):
            if selected[i]:
                # 遍历未加入 MST 的节点
                for j in range(num_vertices):
                    if not selected[j] and graph[i][j] != 0:
                        if graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            u, v = i, j
        if u != -1 and v != -1:
            mst_edges.append((u, v, graph[u][v]))
            selected[v] = True
            edge_count += 1

    return mst_edges

# 使用示例
# if __name__ == "__main__":
#     # 图的邻接矩阵表示，0 表示没有直接边
#     graph = [
#         [0, 2, 0, 6, 0],
#         [2, 0, 3, 8, 5],
#         [0, 3, 0, 0, 7],
#         [6, 8, 0, 0, 9],
#         [0, 5, 7, 9, 0]
#     ]
#
#     mst = prim_for(graph)
#     print("最小生成树的边及权重如下:")
#     for u, v, w in mst:
#         print(f"{u} - {v} : {w}")