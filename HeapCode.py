


class MyHeap:
    def __init__(self,numbers:list):
        self.heap = numbers
    # 返回给定元素的父节点索引
    def parent(self,i):
        return int((i+1)/2)-1
    #返回给定下标元素的左节点
    def left(self,i):
        return 2*(i+1) - 1
    # 返回给定下标元素的右节点
    def right(self,i):
        return 2*(i+1)
    # 利用二叉树性质时间复杂度是O(nlogn)
    def buildMyBigheap(self):
        length = len(self.heap)
        i = 1
        while i < length:
            k = i
            # 找父节点
            while self.parent(k) >= 0:
                parentP = self.parent(k)
                if self.heap[i] > self.heap[parentP]:
                    self.heap[i], self.heap[parentP] = self.heap[parentP], self.heap[i]
                    k = parentP
                else:
                    break
            i += 1

    def heapify_down(self,i):
        n = len(self.heap)
        largest = i  # 假设当前节点是最大的
        left = self.left(i)  # 左孩子
        right = self.right(i)  # 右孩子
        # 如果左孩子存在且比当前节点大
        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        # 如果右孩子存在且比当前最大值大
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        # 如果最大值不是当前节点，需要交换并继续调整
        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            # 递归调整被影响的子树
            self.heapify_down(largest)
    def build_heap_standard(self):
        n = len(self.heap)
        # 从最后一个非叶子节点开始，向前遍历
        start_index = n // 2 - 1  # 最后一个非叶子节点的索引

        for i in range(start_index, -1, -1):  # 从后往前
            self.heapify_down(self.heap, n, i)    # 从底向上构建堆的时间复杂度是O(n)
    def buildMyBigForFloyd(self):
        length = len(self.heap) - 1

        while length >= 0:
            l = self.left(length)
            r = self.right(length)
            idx = length
            number = self.heap[length]
            if l < length and self.heap[l] > self.heap[length]:
                idx = l
                number = self.heap[l]
            if r < length and self.heap[r] > number:
                idx = r
            self.heap[idx], self.heap[length] = self.heap[length], self.heap[idx]
            length -= 1

