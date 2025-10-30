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