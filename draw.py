import matplotlib.pyplot as plt
import numpy as np
import math
# 绝地求生的圈统一时间缩
class Pubg:
    # 计算几个点计划是个点
    def __init__(self,x1:int,y1:int,r1:int,x2:int,y2:int,r2:int,time:int,resulation):
        self.numpoints = resulation
        self.angle = 360/self.numpoints
        self.point = [ i*self.angle for i in range(self.numpoints)]
        self.point1 = [[x1+r1*math.cos(math.radians(self.point[i])),y1+r1*math.sin(math.radians(self.point[i]))] for i in range(self.numpoints)]
        self.point2 = [[x2+r2*math.cos(math.radians(self.point[i])),y2+r2*math.sin(math.radians(self.point[i]))] for i in range(self.numpoints)]
        self.time = time
        self.distancearr = [self.distance(self.point1[i],self.point2[i]) for i in range(self.numpoints) ]
        #print(self.point1)
    def distance(self,r1:list,r2:list):
        return math.sqrt(r1[0]**2+r2[0]**2+r1[1]**2+r2[1]**2)
    def calculate(self):
        t = self.time
        # 计算速度
        n= len(self.point)
        speed = [0]*n
        for i in range(n):
            speed[i] = self.distancearr[i]/t
        return speed
    def result(self,t:int):
        # 计算向量

        direct = [[(self.point1[i][0]-self.point2[i][0])/self.distancearr[i],(self.point1[i][1]-self.point2[i][1])/self.distancearr[i]] for i in range(self.numpoints)]
        print(direct)
        speed  = self.calculate()
        res = []
        for i in range(self.numpoints):
            distanceT = t*speed[i]
            temp = [self.point2[i][0]+distanceT*direct[i][0],self.point2[i][1]+distanceT*direct[i][1]]
            res.append(temp[:])
        return res
class Draw:
    # resulution 表示把圆可以切分多少个点，按照圆的角度平均切分获得
    # x1,y1,r1,x2,y2 ,r2表示各个 圆的圆心和半径
    # time表示多长时间进行缩圆完成
    def __init__(self,resolution,x1,y1,r1,x2,y2,r2,time):
        s = Pubg(x1,y1,r1,x2,y2,r2,time,resolution)
    # 您提供的点坐标数据
        points1 = s.result(9.8) # 完整数据见原始问题

    # 转换为NumPy数组
        points1 = np.array(points1)
        points2 = np.array(s.point1)

        x1, y1 = points1[:, 0], points1[:, 1]
        x2, y2 = points2[:, 0], points2[:, 1]

        # 创建图形
        plt.figure(figsize=(10, 8), dpi=100)

        # 绘制第一个数据集（蓝色）
        plt.plot(x1, y1, 'b-', linewidth=2, label='原始圆形')
        plt.scatter(x1, y1, s=5, c='blue', alpha=0.5)

        # 绘制第二个数据集（红色）
        plt.plot(x2, y2, 'r-', linewidth=2, label='新数据集')
        plt.scatter(x2, y2, s=5, c='red', alpha=0.5)

        # 设置图形属性
        plt.title('双数据集可视化对比', fontsize=16, fontweight='bold')
        plt.xlabel('X轴', fontsize=12)
        plt.ylabel('Y轴', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.axis('equal')  # 确保X/Y轴等比例显示
        plt.legend(loc='best', fontsize=12)

        # 添加参考元素
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.plot(0, 0, 'ko', markersize=8, label='原点')  # 原点标记

        # 添加说明文本
        plt.figtext(0.5, 0.01,
                    f"数据集1: {len(points1)}个点 | 数据集2: {len(points2)}个点",
                    ha="center", fontsize=10, bbox={"facecolor": "orange", "alpha": 0.2, "pad": 5})

        # 显示图形
        plt.tight_layout()
        plt.show()