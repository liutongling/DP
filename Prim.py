import math
from queue import PriorityQueue

# 定义一个优先队列

class Prim:
    def __init__(self,M,G:list):
        # 初始化图
        self.g = G
        #存储最小生成树的点集
        self.point = set([i for i in range(M)])
        self.setPath = []
        self.setPoint = set()
        self.res = set()

    def prim_work(self):
        pq = PriorityQueue()
        pq.put((0,0))
        disAll = 0
        while not ((self.setPoint&self.point)==self.point):
            next = pq.get()
            nextP = next[1]
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