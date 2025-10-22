import sys

import queue
from Dp import TreeNode


def dfs_coins(coins:list,amount:int)->int:
    if amount == 0:
        return 0
    return None


def coinChange( coins: list, amount: int) -> int:
    # 对 coins进行排序
    minNum = sys.maxsize
    if amount!=0 and amount < min(coins):
        return -1
    if amount == 0:
        return 0
    for i in coins:
        if amount >= i:
            next_amount = amount - i
            minNum1 = coinChange(coins, next_amount)
            if minNum1 < minNum and minNum1 != -1:
                minNum = minNum1
    return minNum + 1 if minNum+1 < sys.maxsize else -1

# 实现优先队列
def creat_node(node:list)->list:
    result = []
    for item in node:
        tempNode= TreeNode(item)
        result.append(tempNode)
    return result

def creat_huffman(node:list)->TreeNode:
    res = creat_node(node)
    qu = queue.PriorityQueue()
    for item in res:
        qu.put(item)
    while qu.qsize()>1:
        node1 = qu.get()
        node2 = qu.get()
        tempNode = TreeNode(node2.val+node1.val)
        tempNode.right = node1
        tempNode.left = node2
        qu.put(tempNode)
    return qu.get()
# 查看二叉树，查看每一层
def view_tree(root:TreeNode)->list:
    qu = queue.Queue()
    qu1 = queue.Queue()
    qu.put(root)
    qu1.put(qu)
    result = []
    while not qu1.empty():
        temp1 = qu1.get()
        temp = []
        newqu = queue.Queue()
        while not temp1.empty():
            node = temp1.get()
            temp.append(node.val)
            if node.left:
                newqu.put(node.left)
            if node.right:
                newqu.put(node.right)
        result.append(temp[:])
        if not newqu.empty():
            qu1.put(newqu)
    print(result)
    return result
