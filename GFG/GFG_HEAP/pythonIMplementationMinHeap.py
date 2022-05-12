import sys
class MyHeap():
    def __init__(self, maxsize) -> None:
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0] * (maxsize+1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT=1
    
    def parent(self,pos):
        return pos//2
    
    def left(self,pos):
        return 2*pos
    
    def right(self,pos):
        return 2*pos+1
    
    def isLeaf(self,pos):
        return 2*pos > self.size
    
    def swap(self, x, y):
        self.Heap[x], self.Heap[y] = self.Heap[y], self.Heap[x]
    
    def minHeapify(self, pos):
        if not self.isLeaf(pos):
            leftChild = self.Heap[self.left(pos)]
            rightChild = self.Heap[self.right(pos)]
            if self.Heap[pos] > leftChild or self.Heap[pos] > rightChild:
                if leftChild < rightChild:
                    self.swap(pos, self.left(pos))
                    self.minHeapify(self.left(pos))
                else:
                    self.swap(pos, self.right(pos))
                    self.minHeapify(self.right(pos))
    def insert(self, item):
        if self.size >= self.maxsize:
            return -1
        self.size+=1
        self.Heap[self.size] = item
        current = self.size
        while self.Heap[current] < self.Heap[self.parent(current)]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
    
    def print(self):
        for i in range(1, (self.size//2)+1):
            print(f"""Parent : {self.Heap[i]} LeftChild = {self.Heap[self.left(i)]} RightChild = {self.Heap[self.right(i)]}""")
    def minHeap(self):
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
    
    def remove(self):
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-=1
        self.minHeapify(self.FRONT)
        return popped
if __name__ == "__main__":
     
    print('The minHeap is ')
    minHeap = MyHeap(15)
    minHeap.insert(5)
    minHeap.insert(3)
    minHeap.insert(17)
    minHeap.insert(10)
    minHeap.insert(84)
    minHeap.insert(19)
    minHeap.insert(6)
    minHeap.insert(22)
    minHeap.insert(9)
    minHeap.minHeap()
 
    minHeap.print()
    print("The Min val is " + str(minHeap.remove()))

