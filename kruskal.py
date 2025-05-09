import math
from queue import PriorityQueue

class Kruskal:
    def __init__(self,G,node):
        self.g = G
        # 找到所有的边，由于我们使用的是无向图，邻接矩阵转置相同
        self.pq = PriorityQueue()
        for i in range(node):
            for j in range(i+1,node):
                distance = self.g[i][j]
                if distance !=math.inf:
                    self.pq.put((distance,[i,j]))
        self.root = [i for i in range(node)]

    def findRoot(self,x):
        node = x
        while self.root[node]!=node:
            node = self.root[node]
        return node

    def merageRoot(self,x,y):
        xroot = self.findRoot(x)
        yroot = self.findRoot(y)
        if xroot!=yroot:
            self.root[xroot] = yroot
            return True
        else:
            return False

    def kruskal_work(self):
        res = 0
        while not self.pq.empty():
            next = self.pq.get()
            nexti , nextj = next[1][0] , next[1][1]
            if self.merageRoot(nexti,nextj):
                res += next[0]
                print(nexti,nextj,next[0])
        return res