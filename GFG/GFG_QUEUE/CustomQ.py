class CustomQ:
    def __init__(self, capacity) -> None:
        self.front = self.size = 0
        self.rear = capacity-1
        self.capacity = capacity
        self.Q = [None] * capacity
    
    def __repr__(self) -> str:
        return f""""front  : {self.Q[self.front]} ,Rear : {self.Q[self.rear]} size : {self.size} , {self.Q}"""
    def isFull(self):
        return self.size == self.capacity
    
    def isEmpty(self):
        return self.size ==0
    
    def enqueue(self, item):
        if self.isFull():
            print("Q is FULL")
            raise Exception("Q is FULL")
        self.rear = (self.rear +1 )% self.capacity
        self.size+=1
        self.Q[self.rear] = item
        print(self)
        return self
    
    def dequeue(self):
        if self.isEmpty():
            print("Q is empty")
            raise Exception("Q is empty")
        item  = self.Q[self.front]
        self.front = (self.front+1)%self.capacity
        self.size -=1
        print(self)
        return item
    
    def getRear(self):
        if self.isEmpty():
            print("Q is empty")
            raise Exception("Q is empty")
        return self.Q[self.rear]
    
    def getFront(self):
        if self.isEmpty():
            print("Q is empty")
            raise Exception("Q is empty")
        return self.Q[self.front]

q = CustomQ(5)
q.enqueue(10).enqueue(12).enqueue(9).enqueue(11).enqueue(18)
print(q.dequeue())
q.enqueue(12)
print(q.dequeue())
q.enqueue(13)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())

from queue import PriorityQueue