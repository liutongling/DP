import math
from queue import PriorityQueue

class Dijkstra:
    def __init__(self,G,node):
        self.g = G
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