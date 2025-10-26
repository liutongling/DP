


class MyHeap:
    def __init__(self,numbers:list):
        self.heap = numbers
    def parent(self,i):
        return int((i+1)/2)-1

    def left(self,i):
        return 2*(i+1) - 1

    def right(self,i):
        return 2*(i+1)
    # 利用二叉树性质时间复杂度是O(nlogn)
    def buildMyBigheap(self):
        length = len(self.heap)

        k = 1
        while k < length:
            i = k
            while i > 0:
                # 找父节点
                parentP = self.parent(i)
                if self.heap[i] > self.heap[parentP]:
                    self.heap[i], self.heap[parentP] = self.heap[parentP], self.heap[i]
                    i = parentP
                else:
                    break
            k += 1
    # 从底向上构建堆的时间复杂度是O(n)
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
