from curses.ascii import ENQ


class CircularQ () :
    def __init__(self, size) -> None:
        self.Q = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1
    
    def enqueue(self, item):
        if (self.rear +1 ) % self.size == self.front:
            print("Q is full")
            self.display()
            return False
        if self.front == -1:
            self.front = 0
            self.rear = 0
            self.Q[self.front] = item
            self.display()
            return True
        self.rear = (self.rear+1)%self.size
        self.Q[self.rear] = item
        self.display()
    
    def dequeue(self):
        if self.front == -1:
            print("NOthing to return")
            self.display()
            return False
        # FOR single element
        if self.rear == self.front:
            t = self.Q[self.front]
            self.Q[self.front] = None
            self.rear = -1
            self.front = -1
            print (t)
            self.display()
        else:
            # more than one element.
            t = self.Q[self.front]
            self.Q[self.front] = None
            self.front = (self.front+1)%self.size
            print(t) 
            self.display()
    def display(self):
        print(self.Q)
    def display1(self):
        if self.front == -1:
            print("EMpty Q")
        elif self.rear >= self.front:
            for i in range(self.front, self.rear+1):
                print(self.Q[i], end=" ")
            print()
        else:
            for i in range(self.front, self.size):
                print(self.Q[i], end=" ")
            for j in range(0, self.rear+1):
                print(self.Q[j], end=" ")
            print()
        if (self.rear+1) % self.size  == self.front:
            print("Q is full")
if __name__ == "__main__":
    q = CircularQ(5)
    q.dequeue()
    q.enqueue(14)
    q.enqueue(13)
    q.enqueue(15)
    q.enqueue(16)
    q.enqueue(17)
    q.dequeue()
    q.dequeue()
    q.enqueue(18)
    q.enqueue(19)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.dequeue()
    q.enqueue(21)