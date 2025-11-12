import math
from queue import PriorityQueue

class Dijkstra:
    def __init__(self,G,node):
        self.g = G  # 这个G是一个邻接矩阵表示
        # 找到所有的边，由于我们使用的是无向图，邻接矩阵转置相同
        self.pq = PriorityQueue()#优先队列
        self.node = node # 表示源点
        self.point = set([i for i in range(len(self.g))])#保存所有的点

    def dijkstra_work(self):
        res = 0
        #首先将源点加入进去
        pointNode = set([])
        self.pq.put((0,self.node))
        while not ((pointNode & self.point) ==self.point):
            #print("****")
            next = self.pq.get()
            nextD = next[0]
            nextP = next[1]
            if nextP not in pointNode:
                res += nextD
                pointNode.add(nextP)
                print(nextP,nextD)
                for i in range(len(self.g[nextP])):
                    distanceTemp = self.g[nextP][i]
                    if distanceTemp != math.inf and nextP != i:
                        self.pq.put((distanceTemp+nextD,i))
        return res

class Dijkstra1:
    def __init__(self,node):
        # 初始化邻接表为空
        self.adj = [[] for _ in range(node)]
        # 初始化所有节点都未加入单源最短路径
        self.selected = [False]*node
    def add_edge(self, u, v, w):
        self.adj[u].append((v, w)) # 表示u节点所连的点为v，且权重为w

    def dijkstra_work(self, source:int):
        res = 0
        # 首先将源点加入进去
        pq = PriorityQueue()
        pq.put((0, source)) # 每次取距离源点最近的点
        while not pq.empty():
            nextPoint = pq.get()
            nextWeight = nextPoint[0] #获得最近顶点
            nextPoint = nextPoint[1] # 距离
            if not self.selected[nextPoint]: # 避免重复的节点
                print("This Point is %d,The distance is:%d "% (nextPoint, nextWeight))
                self.selected[nextPoint] = True
                for i in range(len(self.adj[nextPoint])):# 通过邻接表将相邻的点加入堆中
                    nW = self.adj[nextPoint][i][1]
                    nP = self.adj[nextPoint][i][0]
                    distanceTemp = nW+nextWeight
                    if not self.selected[nP]: # 要判断是否该点已经在集合中，避免重复计算
                        pq.put((distanceTemp,nP))
        return res