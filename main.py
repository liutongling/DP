from recall import *
import heapq
from bound import *



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

    # capacity = 5
    # weights = [2,4,5,3]
    # values = [12,16,15,6]
    # capacity = 5
    # weights = [1,2,3]
    # values = [3,3.2,3.3]
    # n = len(values)
    #
    # max_profit, selected_items = branch_and_bound_knapsack1(capacity, weights, values, n)
    #
    # print("最大价值:", max_profit)
    # print("选择的物品索引:", selected_items)
    # print("对应的重量:", [weights[i] for i in selected_items])
    # print("对应的价值:", [values[i] for i in selected_items])

#     print("***************")
#     s = Recall()
#     l = s.recallKnap(weights, values, capacity)
#     print(l)
#     print("***************")
#     s = Recall()
    #task = [[9,2,7,8],[6,4,3,7],[5,8,1,8],[7,6,9,4]]
    #task = [[2, 3, 8],[7, 6, 5],[9, 4, 7]]
    task =[[3,7],[2, 5]]

    mission_problem(task)