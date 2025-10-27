def parent(i):
    return int((i + 1) / 2) - 1


# 返回给定下标元素的左节点
def left(i):
    return 2 * (i + 1) - 1


# 返回给定下标元素的右节点
def right(i):
    return 2 * (i + 1)

def maxify_heap(heap:list,size:int)->list:
    parents =0
    while left(parents)<size or right(parents)<size:
        maxnum = heap[parents]
        child = parents
        if left(parents)<size and maxnum<heap[left(parents)]:
            maxnum = heap[left(parents)]
            child = left(parents)
        if right(parents)<size and maxnum<heap[right(parents)]:
            maxnum = heap[right(parents)]
            child =right(parents)
        if child == parent:#此时感说明往下已经满足大顶堆性质
            return
        #进行交换
        heap[parents],heap[child]= heap[child],heap[parents]
        # 将子节点赋值给parents,然后继续循环
        parents = child